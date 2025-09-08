#!/bin/bash
set -euo pipefail

echo "🚀 一键启动：无人超市管理系统"

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

# 0) 工具与环境
if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ 未检测到 Python3，请先安装 Python3 (>=3.8)"
  exit 1
fi

get_py_ver() { python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")'; }
PY_VER="$(get_py_ver)"
PY_MAJ="${PY_VER%%.*}"
PY_MIN="${PY_VER##*.}"
OS_NAME="$(uname -s)"

# 读取 config.ini 的 [sql] 类型（mysql/mssql）
get_sql_type() {
  awk -F'=' '
    BEGIN{found=0}
    /^\[sql\]/{found=1; next}
    /^\[/{if(found==1) exit}
    found && tolower($1) ~ /^[[:space:]]*type[[:space:]]*$/ {
      gsub(/[[:space:]]/, "", $2);
      print tolower($2);
      exit
    }
  ' config.ini 2>/dev/null || echo "mysql"
}
SQL_TYPE="$(get_sql_type)"
SQL_TYPE_LOWER="$(printf '%s' "$SQL_TYPE" | tr '[:upper:]' '[:lower:]')"

echo "📦 Python: $(python3 -V)"
echo "🗄️  数据库类型: ${SQL_TYPE_LOWER}"
echo "💻 系统: ${OS_NAME}"

# 1) 创建并启用虚拟环境
if [ ! -d ".venv" ]; then
  echo "📦 创建虚拟环境 .venv ..."
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

# 2) 预处理 requirements.txt，生成 requirements.tmp.txt
prepare_requirements() {
  local in="requirements.txt"
  local out="requirements.tmp.txt"
  if [ ! -f "$in" ]; then
    echo "⚠️ 未找到 requirements.txt，跳过依赖安装"
    return 1
  fi
  : > "$out"

  while IFS= read -r line || [ -n "$line" ]; do
    # 去除首尾空白
    l="$(printf '%s' "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
    # 保留空行和注释
    if [ -z "$l" ] || [[ "$l" =~ ^# ]]; then
      echo "$line" >> "$out"
      continue
    fi

    # 修正常见问题
    # 1) MarkupSafe== 1.1.1 -> MarkupSafe==1.1.1
    l="$(printf '%s' "$l" | sed 's/^MarkupSafe==[[:space:]]\+/MarkupSafe==/I')"
    # 2) itsdangerous==1. -> itsdangerous==1.1.0
    l="$(printf '%s' "$l" | sed -E 's/^itsdangerous==1\.$/itsdangerous==1.1.0/I')"

    # 3) macOS/Linux 且非 MSSQL 时跳过 pymssql
    if echo "$l" | grep -qi '^pymssql'; then
      if [ "$OS_NAME" != "Windows_NT" ] && [ "$SQL_TYPE_LOWER" != "mssql" ]; then
        echo "# skipped (not Windows or not mssql): $l" >> "$out"
        continue
      fi
    fi

    # 4) Python >= 3.12 时强制使用 requests>=2.31.0
    if echo "$l" | grep -qi '^requests'; then
      if [ "$PY_MAJ" -ge 3 ] && [ "$PY_MIN" -ge 12 ]; then
        l="requests>=2.31.0"
      fi
    fi

    echo "$l" >> "$out"
  done < "$in"

  return 0
}

echo "🔧 处理依赖文件 ..."
if prepare_requirements; then
  echo "📥 安装依赖（优先使用处理后的 requirements.tmp.txt）..."
  pip install --upgrade pip >/dev/null 2>&1 || true
  if ! pip install -r requirements.tmp.txt; then
    echo "⚠️ 使用处理后依赖失败，回退到原始 requirements.txt ..."
    pip install -r requirements.txt
  fi
else
  echo "⚠️ 无法处理 requirements.txt，尝试直接安装原始依赖 ..."
  pip install -r requirements.txt || true
fi

# 3) 日志目录
mkdir -p logs

# 4) MySQL 端口提示（不阻断）
if ! lsof -Pi :3306 -sTCP:LISTEN -t >/dev/null 2>&1; then
  echo "⚠️ 提示：未检测到 3306 端口监听，请确认 MySQL 已启动且 config.ini 配置正确"
fi

# 5) 初始化数据库（仅第一次）
if [ ! -f ".db_initialized" ]; then
  echo "🗄️ 首次运行，初始化数据库和表 ..."
  set +e
  python3 manage.py initsql --ini config.ini
  python3 manage.py create_all
  python3 manage.py replace_admin
  INIT_EXIT=$?
  set -e
  if [ $INIT_EXIT -ne 0 ]; then
    echo "⚠️ 数据库初始化可能存在问题，请检查 MySQL 配置与服务状态（config.ini / MySQL 是否启动）。"
  else
    touch .db_initialized
    echo "✅ 数据库初始化完成（已创建 .db_initialized 标记）"
  fi
else
  echo "⏭️ 检测到 .db_initialized，跳过数据库初始化"
fi

# 5.5) 构建前端 Admin（查看最新样式）
ADMIN_DIR="$PROJECT_DIR/api/templates/front/admin"
if [ -d "$ADMIN_DIR" ]; then
  echo "🧱 构建前端 Admin ..."
  pushd "$ADMIN_DIR" >/dev/null
  if [ -f "./build.sh" ]; then
    # 通过 tee 记录日志，已启用 pipefail，构建失败会中断脚本
    bash ./build.sh | tee "$PROJECT_DIR/logs/admin_build.log"
  else
    echo "⚠️ 未找到 $ADMIN_DIR/build.sh，跳过前端构建"
  fi
  popd >/dev/null
else
  echo "⚠️ 未找到前端目录 $ADMIN_DIR，跳过前端构建"
fi

# 6) 释放 8080 端口
if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null ; then
  echo "🔧 端口 8080 被占用，正在释放 ..."
  kill -9 $(lsof -t -i:8080) 2>/dev/null || true
  sleep 1
fi

# 7) 启动服务
echo "🌐 启动 Web 服务 ..."
nohup python3 manage.py run > logs/app.log 2>&1 &

# 8) 等待端口就绪
echo -n "⏳ 等待服务启动"
for i in {1..30}; do
  if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null ; then
    echo ""
    break
  fi
  echo -n "."
  sleep 1
done

URL="http://localhost:8080/admin"
echo "✅ 启动成功！"
echo "📱 管理端访问地址: $URL"
echo "📝 日志文件: $PROJECT_DIR/logs/app.log"

# 9) 打开浏览器
if command -v open >/dev/null 2>&1; then
  echo "🔗 正在打开浏览器 ..."
  open "$URL"
fi

echo "🛑 停止服务命令：kill -9 \$(lsof -t -i:8080)"