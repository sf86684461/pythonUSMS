<template>
	<div class="breadcrumb-preview">
		<el-breadcrumb :style='{"width":"100%","lineHeight":"normal","fontSize":"14px","background":"none","display":"flex"}' separator=">">
			<transition-group name="breadcrumb" class="box">
				<el-breadcrumb-item v-for="(item,index) in levelList" :key="item.path">
					<span v-if="item.redirect==='noRedirect'||index==levelList.length-1" class="no-redirect">
            {{ generateTitle(item.meta && item.meta.title ? item.meta.title : item.name) }}
          </span>
					<a v-else @click.prevent="handleLink(item)">
            {{ generateTitle(item.meta && item.meta.title ? item.meta.title : item.name) }}
					</a>
				</el-breadcrumb-item>
			</transition-group>
		</el-breadcrumb>
	</div>
</template>

<script>
import pathToRegexp from 'path-to-regexp'
import { generateTitle } from '@/utils/i18n'
export default {
  data() {
    return {
      levelList: null
    }
  },
  watch: {
    $route() {
      this.getBreadcrumb()
    }
  },
  created() {
    this.getBreadcrumb()
  },
  methods: {
    generateTitle,
    getBreadcrumb() {
      // only show routes with meta.title
      let route = this.$route
      let matched = route.matched.filter(item => item.meta)
      const first = matched[0]
      matched = [{ path: '/index' }].concat(matched)

      this.levelList = matched.filter(item => item.meta)
    },
    isDashboard(route) {
      const name = route && route.name
      if (!name) {
        return false
      }
      return name.trim().toLocaleLowerCase() === 'Index'.toLocaleLowerCase()
    },
    pathCompile(path) {
      // To solve this problem https://github.com/PanJiaChen/vue-element-admin/issues/561
      const { params } = this.$route
      var toPath = pathToRegexp.compile(path)
      return toPath(params)
    },
    handleLink(item) {
      const { redirect, path } = item
      if (redirect) {
        this.$router.push(redirect)
        return
      }
      if(path){
      		  this.$router.push(path)
      }else{
      		  this.$router.push('/')
      }
    },
  }
}
</script>

<style lang="scss" scoped>
	.el-breadcrumb {
		& ::v-deep .el-breadcrumb__separator {
		  		  margin: 0 6px;
		  		  color: #c0c4cc;
		  		  font-weight: 400;
		  		  font-size: 12px;
		  		}
		
		& ::v-deep .el-breadcrumb__inner a {
		  		  color: #409EFF;
		  		  font-weight: 500;
		  		  display: inline-block;
            transition: color .2s ease;
		  		}
    & ::v-deep .el-breadcrumb__inner a:hover {
            color: #66b1ff;
          }
		& ::v-deep .el-breadcrumb__inner {
		  		  color: #606266;
		  		  display: inline-block;
		  		}
    & ::v-deep .el-breadcrumb__item:last-child .el-breadcrumb__inner {
            color: #303133;
            font-weight: 600;
          }
	}
</style>
