<template>
  <div class="dashboard-container">
    <!-- 顶部数据概览 -->
    <div class="stats-grid">
      <div class="stat-card" v-for="(card, idx) in statCards" :key="idx">
        <div class="stat-card__top">
          <span class="stat-card__title">{{ card.title }}</span>
          <span class="pill">{{ card.pill }}</span>
        </div>
        <div class="stat-card__value">{{ card.value }}</div>
        <div class="stat-card__meta">
          周环比：
          <span :class="{'up': card.weekRatio > 0, 'down': card.weekRatio < 0}">
            {{ (card.weekRatio>0?'+':'') + (card.weekRatio*100).toFixed(2) }}%
          </span>
          <span class="yesterday">昨日：{{ card.yesterday }}</span>
        </div>
      </div>
    </div>
    <el-row :gutter="16" class="middle-row" type="flex" align="stretch">
      <el-col :span="10">
        <div class="panel-card">
          <div class="panel-header">
            <span class="panel-title">待办事项</span>
          </div>
          <div class="todo-list">
            <div class="todo-item" v-for="t in todos" :key="t.text">
              <div class="todo-icon" :style="{background:t.bg}">
                <i :class="t.icon"></i>
              </div>
              <span class="todo-text">{{ t.text }}</span>
              <span class="todo-count">{{ t.count }}</span>
            </div>
          </div>

          <!-- 快捷入口 -->
          <div class="quick-grid">
            <div class="quick-item" v-for="q in quicks" :key="q.text" @click="$router.push(q.to)">
              <div class="quick-icon">
                <i :class="q.icon"></i>
              </div>
              <div class="quick-text">{{ q.text }}</div>
            </div>
          </div>
        </div>
      </el-col>

      <el-col :span="14">
        <div class="panel-card">
          <div class="panel-header">
            <span class="panel-title">交易趋势</span>
            <div class="range-tabs">
              <span v-for="r in ranges" :key="r" class="range-item" :class="{active: r===activeRange}">{{ r }}</span>
            </div>
          </div>
          <div id="trendChart" class="chart-box"></div>
        </div>
      </el-col>
    </el-row>

    <!-- 底部：排行榜 + 成交路径 -->
    <el-row :gutter="16" class="bottom-row" type="flex" align="stretch">
      <el-col :span="14">
        <div class="panel-card">
          <div class="panel-header">
            <span class="panel-title">商品销量排行榜 Top 10</span>
            <div class="range-tabs">
              <span class="range-item" :class="{active:true}">本月</span>
              <span class="range-item">近30天</span>
              <span class="range-item">近7天</span>
            </div>
          </div>
          <div class="rank-list">
            <div class="rank-item" v-for="(p, i) in rankingData" :key="p.name">
              <div class="rank-index" :class="'no-'+(i+1)">{{ i+1 }}</div>
              <img class="rank-thumb" :src="p.img" alt="">
              <div class="rank-main">
                <div class="rank-name" :title="p.name">{{ p.name }}</div>
                <div class="rank-progress">
                  <div class="rank-progress__bar" :style="{width: p.progress + '%'}"></div>
                </div>
              </div>
              <div class="rank-value">{{ p.value }}</div>
            </div>
          </div>
        </div>
      </el-col>

      <el-col :span="10">
        <div class="panel-card">
          <div class="panel-header">
            <span class="panel-title">成交路径</span>
            <div class="range-tabs">
              <span class="range-item">本月</span>
              <span class="range-item">近30天</span>
              <span class="range-item active">近7天</span>
            </div>
          </div>

          <div class="path-summary">
            <div class="summary-row"><span>访客人数</span><b>{{ funnel.visitor }}</b></div>
            <div class="summary-row"><span>下单人数</span><b>{{ funnel.order }}</b><em>转化率 {{ funnel.orderRate }}</em></div>
            <div class="summary-row"><span>支付人数</span><b>{{ funnel.pay }}</b><em>转化率 {{ funnel.payRate }}</em></div>
          </div>
          <div id="funnelChart" class="chart-box small"></div>

          <div class="path-footer">
            <div class="footer-cell">
              <span>支付金额</span>
              <b>{{ summary.payAmount }}</b>
            </div>
            <div class="footer-cell">
              <span>客单价</span>
              <b>{{ summary.avgPrice }}</b>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'AdminHome',
  data() {
    return {
      // 顶部指标卡
      statCards: [
        { title: '新增用户', value: 120, weekRatio: 2.25, yesterday: 100, pill: '今日' },
        { title: '浏览量', value: 5890, weekRatio: -0.23, yesterday: 9340, pill: '今日' },
        { title: '访客数', value: 345, weekRatio: 0.23, yesterday: 301, pill: '今日' },
        { title: '订单数量', value: 113, weekRatio: 0.07, yesterday: 140, pill: '今日' },
        { title: '支付金额', value: 15924.09, weekRatio: 0.45, yesterday: 4534.06, pill: '今日' }
      ],
      todos: [
        { icon: 'el-icon-truck', text: '待发货订单', count: 40, bg: '#eaf3ff' },
        { icon: 'el-icon-refresh-left', text: '待退款订单', count: 8, bg: '#eef7ff' },
        { icon: 'el-icon-chat-dot-round', text: '待处理反馈', count: 12, bg: '#edf5ff' }
      ],
      quicks: [
        { icon: 'el-icon-goods', text: '商品管理', to: '/chaoshishangpin' },
        { icon: 'el-icon-user', text: '用户管理', to: '/yonghu' },
        { icon: 'el-icon-document', text: '订单管理', to: '/orders/已支付' },
        { icon: 'el-icon-present', text: '系统管理', to: '/config' }
      ],
      ranges: ['本月', '上月', '近7天'],
      activeRange: '近7天',
      // 排行榜模拟数据
      rankingData: [
        { name: 'NO.1 NALEONPAUL保罗POLO衫男士短袖夏季新款纯棉高速商务休闲体恤翻领印花套装 2061宝蓝', value: 45, progress: 100, img: 'https://images.unsplash.com/photo-1595876227829-985bd38c7512?q=80&w=2448&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
        { name: 'NO.2 Gucci 白色休闲鞋', value: 38, progress: 84, img: 'https://images.unsplash.com/photo-1575176648002-f2021e56b375?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
        { name: 'NO.3 苹果蓝牙耳机', value: 32, progress: 71, img: 'https://images.unsplash.com/photo-1606741965509-717b9fdd6549?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
        { name: 'NO.3 头戴式耳机', value: 28, progress: 62, img: 'https://plus.unsplash.com/premium_photo-1680346528789-0ffcc13f5ebf?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
        { name: 'NO.5 夏季圆领T恤套装 运动休闲 浅蓝色单T恤', value: 18, progress: 40, img: 'https://images.unsplash.com/photo-1654432007491-8c97c473a7b4?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
        { name: 'NO.6 夏季速干运动T恤 男士休闲圆领 舒适透气 灰色', value: 15, progress: 32, img: 'https://images.unsplash.com/photo-1695918428487-7934244c19ac?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' }
      ],
      funnel: { visitor: 345, order: 113, pay: 80, orderRate: '32.8%', payRate: '70.8%' },
      summary: { payAmount: '15924.09', avgPrice: '199.05' },
      trendChart: null,
      funnelChart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initTrendChart()
      this.initFunnelChart()
    })
  },
  beforeDestroy() {
    if (this.trendChart) { this.trendChart.dispose(); this.trendChart = null }
    if (this.funnelChart) { this.funnelChart.dispose(); this.funnelChart = null }
  },
  methods: {
    initTrendChart() {
      const el = document.getElementById('trendChart')
      if (!el) return
      this.trendChart = echarts.init(el)
      const option = {
        grid: { left: 20, right: 20, top: 40, bottom: 20, containLabel: true },
        tooltip: { trigger: 'axis' },
        legend: { data: ['下单数量', '支付金额'], right: 10, top: 10 },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['7.1','7.2','7.3','7.4','7.5','7.6','7.7'],
          axisLine: { lineStyle: { color: '#e6eaf2' } },
          axisLabel: { color: '#8a94a6' }
        },
        yAxis: [
          { type: 'value', axisLine: { show: false }, splitLine: { lineStyle: { color: '#eef2f8' } }, axisLabel: { color: '#8a94a6' } },
          { type: 'value', axisLine: { show: false }, splitLine: { show: false }, axisLabel: { color: '#8a94a6' } }
        ],
        series: [
          {
            name: '下单数量',
            type: 'line',
            smooth: true,
            symbol: 'circle',
            symbolSize: 6,
            itemStyle: { color: '#4b8cff' },
            areaStyle: { color: new echarts.graphic.LinearGradient(0,0,0,1,[{ offset: 0, color: 'rgba(75,140,255,0.45)' },{ offset: 1, color: 'rgba(75,140,255,0.05)' }]) },
            data: [140,160,120,180,150,210,180],
            yAxisIndex: 0
          },
          {
            name: '支付金额',
            type: 'line',
            smooth: true,
            symbol: 'circle',
            symbolSize: 6,
            itemStyle: { color: '#ff7b9c' },
            areaStyle: { color: new echarts.graphic.LinearGradient(0,0,0,1,[{ offset: 0, color: 'rgba(255,123,156,0.35)' },{ offset: 1, color: 'rgba(255,123,156,0.05)' }]) },
            data: [1.6,2.8,1.3,2.2,2.6,3.1,2.5],
            yAxisIndex: 1
          }
        ]
      }
      this.trendChart.setOption(option)
      window.addEventListener('resize', this.trendChart.resize)
    },
    initFunnelChart() {
      const el = document.getElementById('funnelChart')
      if (!el) return
      this.funnelChart = echarts.init(el)
      const option = {
        tooltip: { trigger: 'item', formatter: '{b}: {c}' },
        series: [
          {
            type: 'funnel',
            left: '8%', top: 10, width: '84%', height: '80%',
            sort: 'none', gap: 6,
            label: { show: true, position: 'inside', color: '#fff', formatter: '{b}' },
            labelLine: { show: false },
            itemStyle: { opacity: 0.95 },
            data: [
              { value: this.funnel.visitor, name: '访客', itemStyle: { color: '#7aa9ff' } },
              { value: this.funnel.order,   name: '下单', itemStyle: { color: '#b7d0ff' } },
              { value: this.funnel.pay,     name: '支付', itemStyle: { color: '#dde8ff' } }
            ]
          }
        ]
      }
      this.funnelChart.setOption(option)
      window.addEventListener('resize', this.funnelChart.resize)
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-container {
  padding: 20px;
  background-color: #f6f8fc;
}

/* 顶部统计卡 - 已采用 Grid 等分，保证左右对齐 */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  margin-bottom: 16px;
}
.stats-row { margin-bottom: 16px; }
.stat-card {
  background: #fff;
  border-radius: 10px;
  padding: 16px 16px 12px;
  box-shadow: 0 6px 16px rgba(31,35,41,0.04), 0 3px 6px rgba(31,35,41,0.04);
}
.stat-card__top {
  display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;
}
.stat-card__title { color: #64748b; font-size: 13px; }
.pill {
  background: #edf5ff; color: #4b8cff; border-radius: 12px; padding: 2px 8px; font-size: 12px;
}
.stat-card__value { font-size: 26px; font-weight: 700; color: #1f2937; margin: 4px 0 8px; }
.stat-card__meta { color: #94a3b8; font-size: 12px; }
.stat-card__meta .up { color: #f56c6c; font-weight: 600; margin-right: 10px; }
.stat-card__meta .down { color: #67c23a; font-weight: 600; margin-right: 10px; }
.stat-card__meta .yesterday { margin-left: 10px; }

/* 卡片通用 */
.panel-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 6px 16px rgba(31,35,41,0.04), 0 3px 6px rgba(31,35,41,0.04);
  padding: 12px 16px 16px;
}
.panel-header {
  display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;
}
.panel-title { font-size: 16px; font-weight: 700; color: #1f2937; }
.range-tabs { display: flex; gap: 10px; }
.range-item {
  font-size: 12px; color: #64748b; cursor: pointer; padding: 4px 8px; border-radius: 8px;
}
.range-item.active { background: #edf5ff; color: #4b8cff; }

/* 待办 + 快捷入口 */
.todo-list { padding: 6px 4px 8px; }
.todo-item {
  display: flex; align-items: center; padding: 12px 2px; border-bottom: 1px solid #f3f4f6;
}
.todo-item:last-child { border-bottom: none; }
.todo-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px; }
.todo-icon i { font-size: 18px; color: #4b8cff; }
.todo-text { flex: 1; color: #334155; font-size: 14px; }
.todo-count { color: #4b8cff; font-weight: 700; }

.quick-grid {
  margin-top: 10px;
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;
}
.quick-item {
  background: #f8fafc; border: 1px solid #eef2f7; border-radius: 10px; padding: 12px;
  display: flex; flex-direction: column; align-items: center; cursor: pointer; transition: all .2s;
}
.quick-item:hover { background: #f1f7ff; border-color: #e4efff; transform: translateY(-1px); }
.quick-icon { width: 40px; height: 40px; border-radius: 10px; background: #edf5ff; display: flex; align-items: center; justify-content: center; margin-bottom: 6px; }
.quick-icon i { color: #4b8cff; font-size: 18px; }
.quick-text { color: #334155; font-size: 12px; }

/* 图表盒子 */
.chart-box { width: 100%; height: 300px; }
.chart-box.small { height: 240px; }

.middle-row, .bottom-row { margin-bottom: 16px; }

/* 排行榜 */
.rank-list { display: flex; flex-direction: column; gap: 10px; }
.rank-item {
  display: grid; grid-template-columns: 46px 44px 1fr auto; align-items: center; gap: 10px;
  padding: 8px 6px; border: 1px solid #eef2f7; border-radius: 10px; background: #f9fbff;
}
.rank-index {
  width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center;
  font-weight: 700; color: #fff; background: #aab9d6;
}
.rank-index.no-1 { background: #ff8b6b; }
.rank-index.no-2 { background: #fbbf24; }
.rank-index.no-3 { background: #34d399; }
.rank-thumb { width: 40px; height: 40px; border-radius: 6px; object-fit: cover; background: #e5e7eb; }
.rank-main { overflow: hidden; }
.rank-name { color: #334155; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 6px; }
.rank-progress { width: 100%; height: 6px; background: #eef2f7; border-radius: 999px; }
.rank-progress__bar { height: 100%; background: linear-gradient(90deg, #4b8cff, #7aa9ff); border-radius: 999px; }
.rank-value { font-weight: 700; color: #1f2937; min-width: 32px; text-align: right; }

/* 成交路径 */
.path-summary { display: flex; flex-direction: column; gap: 8px; margin: 6px 0 8px; }
.summary-row { display: flex; align-items: center; justify-content: space-between; color: #475569; font-size: 14px; }
.summary-row b { color: #111827; font-size: 16px; }
.summary-row em { font-style: normal; color: #4b8cff; font-size: 12px; margin-left: 8px; }

.path-footer {
  margin-top: 8px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
}
.footer-cell {
  background: #f8fafc; border: 1px solid #eef2f7; border-radius: 10px; padding: 12px; text-align: center;
}
.footer-cell span { color: #64748b; font-size: 12px; display: block; }
.footer-cell b { color: #111827; font-size: 18px; }

/* 行启用 Flex，列等高 */
.middle-row, .bottom-row {
  margin-bottom: 16px;
  display: flex;           /* 关键：行本身是 flex */
  align-items: stretch;    /* 两列等高 */
}
.middle-row .el-col,
.bottom-row .el-col {
  display: flex;           /* 列作为 flex 容器 */
}
.middle-row .panel-card,
.bottom-row .panel-card {
  flex: 1 1 auto;          /* 卡片填满列高 */
  display: flex;
  flex-direction: column;  /* 便于“贴底” */
}

/* 左右卡片主体可伸展 + 右侧底部统计贴底 */
.bottom-row .rank-list { flex: 1 1 auto; min-height: 0; }
.bottom-row .chart-box.small { flex: 1 1 auto; min-height: 0; }
.bottom-row .path-footer { margin-top: auto; }

/* 待办 + 快捷入口 */
.todo-list { padding: 6px 4px 8px; }
.todo-item {
  display: flex; align-items: center; padding: 12px 2px; border-bottom: 1px solid #f3f4f6;
}
.todo-item:last-child { border-bottom: none; }
.todo-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px; }
.todo-icon i { font-size: 18px; color: #4b8cff; }
.todo-text { flex: 1; color: #334155; font-size: 14px; }
.todo-count { color: #4b8cff; font-weight: 700; }

.quick-grid {
  margin-top: 10px;
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;
}
.quick-item {
  background: #f8fafc; border: 1px solid #eef2f7; border-radius: 10px; padding: 12px;
  display: flex; flex-direction: column; align-items: center; cursor: pointer; transition: all .2s;
}
.quick-item:hover { background: #f1f7ff; border-color: #e4efff; transform: translateY(-1px); }
.quick-icon { width: 40px; height: 40px; border-radius: 10px; background: #edf5ff; display: flex; align-items: center; justify-content: center; margin-bottom: 6px; }
.quick-icon i { color: #4b8cff; font-size: 18px; }
.quick-text { color: #334155; font-size: 12px; }

/* 图表盒子 */
.chart-box { width: 100%; height: 300px; }
.chart-box.small { height: 240px; }

.middle-row, .bottom-row { margin-bottom: 16px; }  /* 已在上面统一控制，可保留 */

/* 排行榜 */
.rank-list { display: flex; flex-direction: column; gap: 10px; }
.rank-item {
  display: grid; grid-template-columns: 46px 44px 1fr auto; align-items: center; gap: 10px;
  padding: 8px 6px; border: 1px solid #eef2f7; border-radius: 10px; background: #f9fbff;
}
.rank-index {
  width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center;
  font-weight: 700; color: #fff; background: #aab9d6;
}
.rank-index.no-1 { background: #ff8b6b; }
.rank-index.no-2 { background: #fbbf24; }
.rank-index.no-3 { background: #34d399; }
.rank-thumb { width: 40px; height: 40px; border-radius: 6px; object-fit: cover; background: #e5e7eb; }
.rank-main { overflow: hidden; }
.rank-name { color: #334155; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 6px; }
.rank-progress { width: 100%; height: 6px; background: #eef2f7; border-radius: 999px; }
.rank-progress__bar { height: 100%; background: linear-gradient(90deg, #4b8cff, #7aa9ff); border-radius: 999px; }
.rank-value { font-weight: 700; color: #1f2937; min-width: 32px; text-align: right; }

/* 成交路径 */
.path-summary { display: flex; flex-direction: column; gap: 8px; margin: 6px 0 8px; }
.summary-row { display: flex; align-items: center; justify-content: space-between; color: #475569; font-size: 14px; }
.summary-row b { color: #111827; font-size: 16px; }
.summary-row em { font-style: normal; color: #4b8cff; font-size: 12px; margin-left: 8px; }

.path-footer {
  margin-top: 8px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
}
.footer-cell {
  background: #f8fafc; border: 1px solid #eef2f7; border-radius: 10px; padding: 12px; text-align: center;
}
.footer-cell span { color: #64748b; font-size: 12px; display: block; }
.footer-cell b { color: #111827; font-size: 18px; }
</style>
