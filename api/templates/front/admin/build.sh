#!/usr/bin/env bash
set -euo pipefail

# 进入脚本所在目录（admin 前端根）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

log() { printf "\033[1;34m==>\033[0m %s\n" "$*"; }
ok()  { printf "\033[1;32m✔\033[0m %s\n" "$*"; }
warn(){ printf "\033[1;33m!\033[0m %s\n" "$*"; }
err() { printf "\033[1;31m✖ %s\033[0m\n" "$*" >&2; exit 1; }

# Node 版本兼容：Node >= 17 需要 legacy OpenSSL 选项（webpack4）
if command -v node >/dev/null 2>&1; then
  NODE_MAJOR="$(node -v | sed -E 's/v([0-9]+).*/\1/')"
  if [ "${NODE_MAJOR:-0}" -ge 17 ]; then
    export NODE_OPTIONS="--openssl-legacy-provider"
    warn "检测到 Node >= 17，已设置 NODE_OPTIONS=--openssl-legacy-provider 以兼容 webpack4"
  fi
else
  err "未检测到 Node，请先安装 Node.js (建议 14.x 或 16.x)"
fi

# 安装依赖（若缺失）
if [ ! -d "node_modules" ]; then
  log "安装依赖（首次或缺失）..."
  npm ci || npm install
  ok "依赖安装完成"
else
  log "检测到 node_modules，跳过安装（如需重新安装请删除 node_modules）"
fi

# 构建到临时目录，再原子替换 dist
BUILD_TMP="dist-build"
TARGET_DIR="${SCRIPT_DIR}/dist"

log "开始构建（输出：${BUILD_TMP})..."
npx vue-cli-service build --dest "${BUILD_TMP}"
ok "构建完成"

log "替换后端静态目录：${TARGET_DIR}"
rm -rf "${TARGET_DIR}"
mv "${BUILD_TMP}" "${TARGET_DIR}"
ok "部署完成：${TARGET_DIR}"

echo
ok "管理端已就绪： http://localhost:8080/admin#/"
echo "如浏览器有缓存，请使用强制刷新(⌘+Shift+R)"