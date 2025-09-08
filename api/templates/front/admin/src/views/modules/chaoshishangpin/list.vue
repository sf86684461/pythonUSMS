<template>
	<div class="main-content" :style='{"color":"#3B3E40","padding":"30px 30px 30px","fontSize":"14px"}'>
		<!-- 列表页 -->
		<template v-if="showFlag">
			<el-form class="center-form-pv" :style='{"border":"0px solid #bababa","padding":"0px","margin":"0px","overflow":"hidden","borderRadius":"0px","flexWrap":"wrap","background":"none","display":"flex","fontSize":"inherit","justifyContent":"space-between"}' :inline="true" :model="searchForm">
				<el-row :style='{"border":"1px solid #e3e3e3","padding":"20px","borderRadius":"5px","textAlign":"center","flexWrap":"wrap","background":"#fff","flexDirection":"row","display":"flex","width":"auto","fontSize":"inherit","justifyContent":"flex-start"}' >
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","flexWrap":"wrap","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">商品名称</label>
						<el-input v-model="searchForm.shangpinmingcheng" placeholder="商品名称" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","flexWrap":"wrap","display":"flex"}'>
						<label :style='{"margin":"0 10px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">价格</label>
						<el-input v-model="searchForm.pricestart" placeholder="最小价格" clearable></el-input>
					</div>
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","flexWrap":"wrap","display":"flex"}' :label="'至'">
						<el-input v-model="searchForm.priceend" placeholder="最大价格" clearable></el-input>
					</div>
					<el-button class="search" type="success" @click="search()">
						<span class="icon iconfont icon-chakan12" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none","height":"40px"}'></span>
						搜索
					</el-button>
				</el-row>

				<el-row class="actions" :style='{"border":"0px solid #e3e3e3","padding":"0px","margin":"20px 0 10px","color":"#fff","textAlign":"left","flexDirection":"row","display":"flex","justifyContent":"flex-start","borderRadius":"5px","flexWrap":"wrap","background":"none","width":"100%","fontSize":"inherit"}'>
					<el-button class="add" v-if="isAuth('chaoshishangpin','新增')" type="success" @click="addOrUpdateHandler()">
						<span class="icon iconfont icon-tianjia13" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
						新增
					</el-button>
					<el-button class="del" v-if="isAuth('chaoshishangpin','删除')" :disabled="dataListSelections.length?false:true" type="danger" @click="deleteHandler()">
						<span class="icon iconfont icon-shanchu7" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none","height":"40px"}'></span>
						删除
					</el-button>



					<el-button class="btn18" v-if="isAuth('chaoshishangpin','库存统计')" type="success" @click="chartDialog1()">
						<span class="icon iconfont icon-a-fenxiang2" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
						库存统计
					</el-button>
				</el-row>
			</el-form>
			<!-- list two -->
			<div class="one" :style='{"border":"1px solid #e3e3e3","padding":"30px 0 0 2%","margin":"30px 0 0","borderRadius":"8px","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","fontSize":"14px","justifyContent":"flex-start","height":"auto"}'>
			  <div v-for="(item,index) in dataList" :style='{"border":"1px solid #e9e9e9","boxShadow":"none","margin":"0 2% 30px 0","borderRadius":"8px","background":"#f7f7f7","width":"23%","position":"relative","height":"auto"}' :key="index">
			    <div :style='{"padding":"5px 10px","lineHeight":"32px","fontSize":"inherit","color":"#666","textAlign":"center","background":"none"}' class="name">{{item.shangpinmingcheng}}</div>
			    <div :style='{"padding":"5px 10px","lineHeight":"32px","fontSize":"inherit","color":"#666","textAlign":"center","background":"none"}' class="name">{{item.gongyingshang}}</div>
				<template v-if="item.shangpintupian">
					<img v-if="item.shangpintupian.substring(0,4)=='http'" :style='{"padding":"10px","margin":"0px","objectFit":"cover","borderRadius":"8px 8px 0 0","display":"block","width":"100%","height":"240px"}' :src="item.shangpintupian.split(',')[0]" />
					<img v-else :style='{"padding":"10px","margin":"0px","objectFit":"cover","borderRadius":"8px 8px 0 0","display":"block","width":"100%","height":"240px"}' :src="$base.url+item.shangpintupian.split(',')[0]" />
				</template>
			    <div :style='{"padding":"10px 10px 10px","margin":"10px 0","alignItems":"flex-start","flexWrap":"wrap","display":"flex","width":"100%","fontSize":"12px","justifyContent":"flex-start","height":"auto"}'>
			      <el-button class="list1-view" v-if=" isAuth('chaoshishangpin','查看')" @click="addOrUpdateHandler(item.id,'info')">
			        <span class="icon iconfont icon-chakan14" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			        浏览
			      </el-button>
			      <el-button class="list1-edit" v-if=" isAuth('chaoshishangpin','修改') " @click="addOrUpdateHandler(item.id)">
			        <span class="icon iconfont icon-qianshuxieyi" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			        更新
			      </el-button>
					<el-button class="list1-view" v-if="isAuth('chaoshishangpin','查看评论')" type="success" @click="disscussListHandler(item.id)">
					  <span class="icon iconfont icon-chakan14" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
					  查看评论
					</el-button>
				  <el-button class="list1-btn8" v-if="isAuth('chaoshishangpin','进货')" @click="shangpinjinhuoCrossAddOrUpdateHandler(item,'cross','','','','')">
				    <span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
				    进货
				  </el-button>
			      <el-button class="list1-del" v-if="isAuth('chaoshishangpin','删除') " @click="deleteHandler(item.id)">
			        <span class="icon iconfont icon-guanbi1" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","display":"none"}'></span>
			        删除
			      </el-button>
			    </div>
			  </div>
			</div>
			<el-pagination
				@size-change="sizeChangeHandle"
				@current-change="currentChangeHandle"
				:current-page="pageIndex"
				background
				:page-sizes="[10, 50, 100, 200]"
				:page-size="pageSize"
				:layout="layouts.join()"
				:total="totalPage"
				prev-text="上一页 "
				next-text="下一页 "
				:hide-on-single-page="false"
				:style='{"padding":"0","margin":"20px 0 0","whiteSpace":"nowrap","color":"inherit","textAlign":"left","width":"100%","fontSize":"inherit","fontWeight":"500"}'
			></el-pagination>
		</template>
		
		<!-- 添加/修改页面  将父组件的search方法传递给子组件-->
		<add-or-update v-if="addOrUpdateFlag" :parent="this" ref="addOrUpdate"></add-or-update>

		<shangpinjinhuo-cross-add-or-update v-if="shangpinjinhuoCrossAddOrUpdateFlag" :parent="this" ref="shangpinjinhuoCrossaddOrUpdate"></shangpinjinhuo-cross-add-or-update>



		<el-dialog
		  :visible.sync="chartVisiable1"
		  width="800">
			<div id="alllimittimesChart1" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog1">返回</el-button>
		  </span>
		</el-dialog>

	</div>
</template>

<script>
import * as echarts from 'echarts'
import chinaJson from "@/components/echarts/china.json";
import axios from 'axios'
import AddOrUpdate from "./add-or-update";
import shangpinjinhuoCrossAddOrUpdate from "../shangpinjinhuo/add-or-update";
	export default {
		data() {
			return {
				searchForm: {
					key: ""
				},
				form:{},
				dataList: [],
				pageIndex: 1,
				pageSize: 10,
				totalPage: 0,
				dataListLoading: false,
				dataListSelections: [],
				showFlag: true,
				chartVisiable1: false,
				addOrUpdateFlag:false,
				shangpinjinhuoCrossAddOrUpdateFlag: false,
				layouts: ["total","prev","pager","next"],
			};
		},
		created() {
			this.init();
			this.getDataList();
			this.contentStyleChange()
		},
		mounted() {
		},
		filters: {
			htmlfilter: function (val) {
				return val.replace(/<[^>]*>/g).replace(/undefined/g,'');
			}
		},
		computed: {
			tablename(){
				return this.$storage.get('sessionTable')
			},
		},
		components: {
			AddOrUpdate,
			shangpinjinhuoCrossAddOrUpdate,
		},
		methods: {
			contentStyleChange() {
				this.contentPageStyleChange()
			},
			// 分页
			contentPageStyleChange(){
				let arr = []

				// if(this.contents.pageTotal) arr.push('total')
				// if(this.contents.pageSizes) arr.push('sizes')
				// if(this.contents.pagePrevNext){
				//   arr.push('prev')
				//   if(this.contents.pagePager) arr.push('pager')
				//   arr.push('next')
				// }
				// if(this.contents.pageJumper) arr.push('jumper')
				// this.layouts = arr.join()
				// this.contents.pageEachNum = 10
			},
			shangpinjinhuoCrossAddOrUpdateHandler(row,type,crossOptAudit,crossOptPay,statusColumnName,tips,statusColumnValue){
				this.showFlag = false;
				this.addOrUpdateFlag = false;
				this.shangpinjinhuoCrossAddOrUpdateFlag = true;
				this.$storage.set('crossObj',row);
				this.$storage.set('crossTable','chaoshishangpin');
				this.$storage.set('statusColumnName',statusColumnName);
				this.$storage.set('statusColumnValue',statusColumnValue);
				this.$storage.set('tips',tips);
				if(statusColumnName!=''&&!statusColumnName.startsWith("[")) {
					var obj = this.$storage.getObj('crossObj');
					for (var o in obj){
						if(o==statusColumnName && obj[o]==statusColumnValue){
							this.$message({
								message: tips,
								type: "success",
								duration: 1500,
								onClose: () => {
									this.getDataList();
								}
							});
							this.showFlag = true;
							this.shangpinjinhuoCrossAddOrUpdateFlag = false;
							return;
						}
					}
				}
				this.$nextTick(() => {
					this.$refs.shangpinjinhuoCrossaddOrUpdate.init(row.id,type);
				});
			},


//统计接口
    chartDialog1() {
      this.chartVisiable1 = !this.chartVisiable1;
      this.$nextTick(()=>{
        var alllimittimesChart1 = echarts.init(document.getElementById("alllimittimesChart1"),'macarons');
        this.$http({
            url: `chaoshishangpin/value/shangpinmingcheng/alllimittimes`,
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].shangpinmingcheng);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].shangpinmingcheng
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '库存统计',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxis,
                        axisLabel : {
                            rotate:40
                        }
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                alllimittimesChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    alllimittimesChart1.resize();
                };
            }
        });
      })
    },




    init () {
          let urlalllimittimes = 'chaoshishangpin/remind/alllimittimes/1';
		urlalllimittimes+=`?remindend=20`,
		
            	urlalllimittimes+=`&remindstart=0`,

          this.$http({
            url: urlalllimittimes,
            method: "get",
          }).then(({ data }) => {
            if (data && data.code == 0 && data.count>0 ) {
              this.$alert(`库存有${data.count}条记录到达预警`)
            }
          });
    },
    search() {
      this.pageIndex = 1;
      this.getDataList();
    },

    // 获取数据列表
    getDataList() {
      this.dataListLoading = true;
      let params = {
        page: this.pageIndex,
        limit: this.pageSize,
        sort: 'id',
        order: 'desc',
      }
           if(this.searchForm.shangpinmingcheng!='' && this.searchForm.shangpinmingcheng!=undefined){
            params['shangpinmingcheng'] = '%' + this.searchForm.shangpinmingcheng + '%'
          }
           if(this.searchForm.pricestart!='' && this.searchForm.pricestart!=undefined ){
            params['pricestart'] = this.searchForm.pricestart
          }
          if(this.searchForm.priceend!='' && this.searchForm.priceend!=undefined){
            params['priceend'] = this.searchForm.priceend
          }
			let user = JSON.parse(this.$storage.getObj('userForm'))
			console.log(user)
			this.$http({
				url: "chaoshishangpin/page",
				method: "get",
				params: params
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.dataList = data.data.list;
					this.totalPage = data.data.total;
				} else {
					this.dataList = [];
					this.totalPage = 0;
				}
				this.dataListLoading = false;
			});
    },
    // 每页数
    sizeChangeHandle(val) {
      this.pageSize = val;
      this.pageIndex = 1;
      this.getDataList();
    },
    // 当前页
    currentChangeHandle(val) {
      this.pageIndex = val;
      this.getDataList();
    },
    // 多选
    selectionChangeHandler(val) {
      this.dataListSelections = val;
    },
    // 添加/修改
    addOrUpdateHandler(id,type) {
      this.showFlag = false;
      this.addOrUpdateFlag = true;
      this.crossAddOrUpdateFlag = false;
      if(type!='info'){
        type = 'else';
      }
      this.$nextTick(() => {
        this.$refs.addOrUpdate.init(id,type);
      });
    },
    // 查看评论
    disscussListHandler(id,type) {
	this.$router.push({path:'/discusschaoshishangpin',query:{refid:id}});
    },
    // 下载
    download(file){
      let arr = file.replace(new RegExp('upload/', "g"), "")
      axios.get(this.$base.url + 'file/download?fileName=' + arr, {
      	headers: {
      		token: this.$storage.get('Token')
      	},
      	responseType: "blob"
      }).then(({
      	data
      }) => {
      	const binaryData = [];
      	binaryData.push(data);
      	const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
      		type: 'application/pdf;chartset=UTF-8'
      	}))
      	const a = document.createElement('a')
      	a.href = objectUrl
      	a.download = arr
      	// a.click()
      	// 下面这个写法兼容火狐
      	a.dispatchEvent(new MouseEvent('click', {
      		bubbles: true,
      		cancelable: true,
      		view: window
      	}))
      	window.URL.revokeObjectURL(data)
      },err=>{
		  axios.get((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] :'') + this.$base.name + '/file/download?fileName=' + arr, {
		  	headers: {
		  		token: this.$storage.get('Token')
		  	},
		  	responseType: "blob"
		  }).then(({
		  	data
		  }) => {
		  	const binaryData = [];
		  	binaryData.push(data);
		  	const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
		  		type: 'application/pdf;chartset=UTF-8'
		  	}))
		  	const a = document.createElement('a')
		  	a.href = objectUrl
		  	a.download = arr
		  	// a.click()
		  	// 下面这个写法兼容火狐
		  	a.dispatchEvent(new MouseEvent('click', {
		  		bubbles: true,
		  		cancelable: true,
		  		view: window
		  	}))
		  	window.URL.revokeObjectURL(data)
		  })
	  })
    },
	// 预览
	preClick(file){
		if(!file){
			return false
		}
		window.open((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] + this.$base.name + '/' + file :this.$base.url + file))
	},
	chaoshishangpinstatusChange(e,row){
		if(row.status==0){
			row.passwordwrongnum = 0
		}
		this.$http({
			url:'chaoshishangpin/update',
			method:'post',
			data:row
		}).then(res=>{
			if(row.status==1){
				this.$message.error('该用户已锁定')
			}else{
				this.$message.success('该用户已解除锁定')
			}
		})
	},
    // 删除
    async deleteHandler(id ) {
		var ids = id? [Number(id)]: this.dataListSelections.map(item => {
			return Number(item.id);
		});
		await this.$confirm(`确定进行[${id ? "删除" : "批量删除"}]操作?`, "提示", {
			confirmButtonText: "确定",
			cancelButtonText: "取消",
			type: "warning"
		}).then(async () => {
			await this.$http({
				url: "chaoshishangpin/delete",
				method: "post",
				data: ids
			}).then(async ({ data }) => {
				if (data && data.code === 0) {
					for(let x in ids){
						await this.$http.get('storeup/list',{params: {
							page: 1,
							limit: 100,
							refid: ids[x],
							tablename: 'chaoshishangpin'
						}}).then(async obj=>{
							if(obj.data&&obj.data.code==0){
								if(obj.data.data.list.length){
									let arr = []
									for(let i in obj.data.data.list){
										arr.push(obj.data.data.list[i].id)
									}
									await this.$http.post('storeup/delete',arr).then(()=>{})
								}
							}
						})
					}
					this.$message({
						message: "操作成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.search();
						}
					});
            
				} else {
					this.$message.error(data.msg);
				}
			});
		});
    },


  }

};
</script>
<style lang="scss" scoped>
	
	.center-form-pv {
	  .el-date-editor.el-input {
	    width: auto;
	  }
	}
	
	.el-input {
	  width: auto;
	}
	
	// form
	.center-form-pv .el-input ::v-deep .el-input__inner {
				border: 1px solid #e3e3e3;
				border-radius: 3px;
				padding: 0 12px;
				color: inherit;
				background: #fff;
				width: 150px;
				font-size: inherit;
				line-height: 34px;
				height: 34px;
			}
	
	.center-form-pv .el-select ::v-deep .el-input__inner {
				border: 1px solid #e3e3e3;
				border-radius: 3px;
				padding: 0 10px;
				color: inherit;
				background: #fff;
				width: 150px;
				font-size: inherit;
				line-height: 34px;
				height: 34px;
			}
	
	.center-form-pv .el-date-editor ::v-deep .el-input__inner {
				border: 1px solid #e3e3e3;
				border-radius: 3px;
				padding: 0 10px 0 30px;
				color: inherit;
				background: #fff;
				width: 150px;
				font-size: inherit;
				line-height: 34px;
				height: 34px;
			}
	
	.center-form-pv .search {
				cursor: pointer;
				padding: 10px 15px;
				margin: 0 10px;
				color: #fff;
				font-size: 14px;
				border-color: #719e37;
				transition: all 0s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #9bc747 0%,#82bd42 100%);
				width: auto;
				border-width: 1px;
				border-style: solid;
				min-width: 80px;
				height: 34px;
			}
	
	.center-form-pv .search:hover {
			}
	
	.center-form-pv .actions .add {
				border: 1px solid #0f70ad;
				cursor: pointer;
				padding: 10px 15px;
				margin: 4px 4px 5px 0;
				color: inherit;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #208ed3 0%,#0272bd 100%),#208ed3;
				width: auto;
				min-width: 70px;
				height: auto;
			}
	
	.center-form-pv .actions .add:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	.center-form-pv .actions .del {
				border: 1px solid #af2b1b;
				cursor: pointer;
				padding: 10px 15px;
				margin: 4px 4px 5px;
				color: inherit;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
				background: linear-gradient(to bottom, #bc3423 0%,#cd4433 100%);
				width: auto;
				min-width: 70px;
				height: auto;
			}
	
	.center-form-pv .actions .del:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	.center-form-pv .actions .statis {
				border: 1px solid #719e37;
				cursor: pointer;
				padding: 10px 15px;
				margin: 4px 4px 5px;
				color: inherit;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #9bc747 0%,#82bd42 100%);
				width: auto;
				height: auto;
			}
	
	.center-form-pv .actions .statis:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	.center-form-pv .actions .btn18 {
				border: 1px solid #323537;
				cursor: pointer;
				padding: 10px 15px;
				margin: 4px 4px 5px;
				color: #fff;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
				background: linear-gradient(to bottom, #4b4f51 0%,#414547 100%);
				width: auto;
				height: auto;
			}
	
	.center-form-pv .actions .btn18:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	// table
	.el-table ::v-deep .el-table__header-wrapper thead {
				color: inherit;
				background: rgba(254,169,34,0);
				width: 100%;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr {
				background: linear-gradient(to bottom, #ededee 0%,#dddddd 100%);
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr th {
				padding: 2px 0;
				background: none;
				border-color: #fff;
				border-width: 0 0px 1px 0;
				border-style: solid;
				text-align: left;
			}

	.el-table ::v-deep .el-table__header-wrapper thead tr th .cell {
				padding: 0 0px;
				word-wrap: normal;
				color: #333;
				white-space: normal;
				font-weight: 600;
				display: flex;
				vertical-align: middle;
				font-size: 12px;
				line-height: 24px;
				text-overflow: ellipsis;
				word-break: break-all;
				width: 100%;
				align-items: center;
				position: relative;
			}

	
	.el-table ::v-deep .el-table__body-wrapper tbody {
				padding: 0;
				width: 100%;
			}

	.el-table ::v-deep .el-table__body-wrapper tbody tr {
				background: none;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td {
				padding: 2px 0;
				color: inherit;
				background: none;
				font-size: inherit;
				border-color: #f4f4f4;
				border-width: 0 0px 1px 0px;
				border-style: solid;
				text-align: left;
			}
	
		.el-table ::v-deep .el-table__body-wrapper tbody tr.el-table__row--striped td {
		background: #f0f0f0;
	}
		
	.el-table ::v-deep .el-table__body-wrapper tbody tr:hover td {
				padding: 2px 0;
				color: #fff;
				background: linear-gradient(to bottom, #208ed3 0%,#0272bd 100%),#208ed3;
				font-weight: 500;
				border-color: #e9e9e9;
				border-width: 0 0px 1px 0px;
				border-style: solid;
				text-align: left;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td {
				padding: 2px 0;
				color: inherit;
				background: none;
				font-size: inherit;
				border-color: #f4f4f4;
				border-width: 0 0px 1px 0px;
				border-style: solid;
				text-align: left;
			}

	.el-table ::v-deep .el-table__body-wrapper tbody tr td .cell {
				padding: 0 0px;
				overflow: hidden;
				color: inherit;
				word-break: break-all;
				white-space: normal;
				display: flex;
				font-size: 12px;
				line-height: 24px;
				text-overflow: ellipsis;
				flex-wrap: wrap;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .view {
				border: 1px solid #0f70ad;
				cursor: pointer;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				color: #fff;
				font-size: 13px;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #208ed3 0%,#0272bd 100%);
				width: auto;
				min-width: 40px;
				height: 30px;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .view:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .add {
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .add:hover {
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .edit {
				border: 1px solid #719e37;
				cursor: pointer;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				color: #fff;
				font-size: 13px;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #9bc747 0%,#82bd42 100%);
				width: auto;
				min-width: 40px;
				height: 30px;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .edit:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .del {
				border: 1px solid #af2b1b;
				cursor: pointer;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				color: #fff;
				font-size: 13px;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
				background: linear-gradient(to bottom, #bc3423 0%,#cd4433 100%);
				width: auto;
				height: 30px;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .del:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .btn8 {
				border: 1px solid #323537;
				cursor: pointer;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				color: #fff;
				font-size: 13px;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
				background: linear-gradient(to bottom, #4b4f51 0%,#414547 100%);
				width: auto;
				height: 30px;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .btn8:hover {
				transform: translate3d(-8px, 0px, 0px);
			}
	
	// pagination
	.main-content .el-pagination ::v-deep .el-pagination__total {
				margin: 0 10px 0 0;
				color: inherit;
				font-weight: 400;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .btn-prev {
				border: none;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: inherit;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .btn-next {
				border: none;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: inherit;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .btn-prev:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: #999;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .btn-next:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: #999;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}

	.main-content .el-pagination ::v-deep .el-pager {
				padding: 0;
				margin: 0;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
			}

	.main-content .el-pagination ::v-deep .el-pager .number {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: inherit;
				background: none;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 24px;
				text-align: center;
				height: 24px;
			}
	
	.main-content .el-pagination ::v-deep .el-pager .number:hover {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: #fff;
				background: #1c84c6;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 24px;
				text-align: center;
				height: 24px;
			}
	
	.main-content .el-pagination ::v-deep .el-pager .number.active {
				cursor: default;
				padding: 0 4px;
				margin: 0 5px;
				color: #fff;
				background: #1c84c6;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 24px;
				text-align: center;
				height: 24px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes {
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input {
				margin: 0 5px;
				color: inherit;
				width: 100px;
				font-size: inherit;
				position: relative;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input .el-input__inner {
				border: 0px solid #ddd;
				cursor: pointer;
				padding: 0 25px 0 8px;
				color: inherit;
				display: inline-block;
				font-size: inherit;
				line-height: 28px;
				border-radius: 3px;
				outline: 0;
				background: none;
				width: 100%;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input span.el-input__suffix {
				top: 0;
				position: absolute;
				right: 0;
				height: 100%;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
				cursor: pointer;
				color: #C0C4CC;
				width: 25px;
				font-size: 14px;
				line-height: 28px;
				text-align: center;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__jump {
				margin: 0 0 0 24px;
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__jump .el-input {
				border-radius: 3px;
				padding: 0 2px;
				margin: 0 2px;
				color: inherit;
				display: inline-block;
				width: 50px;
				font-size: inherit;
				line-height: 18px;
				position: relative;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination ::v-deep .el-pagination__jump .el-input .el-input__inner {
				border: 1px solid #eee;
				cursor: pointer;
				padding: 0 0px;
				color: inherit;
				display: inline-block;
				font-size: inherit;
				line-height: 24px;
				border-radius: 3px;
				outline: 0;
				background: none;
				width: auto;
				text-align: center;
				height: 24px;
			}
	
	// list one
	.one .list1-view {
				border: 1px solid #0f70ad;
				cursor: pointer;
				padding: 0 6px 0 4px;
				margin: 0px 5px 5px 0;
				color: #fff;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #208ed3 0%,#0272bd 100%);
				width: auto;
				min-width: 58px;
				height: 32px;
			}
	
	.one .list1-view:hover {
				transform: translate3d(-6px, 0px, 0px);
			}
	
	.one .list1-edit {
				border: 1px solid #719e37;
				cursor: pointer;
				padding: 0 6px 0 4px;
				margin: 0px 5px 5px 0;
				color: #fff;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
				background: linear-gradient(to bottom, #9bc747 0%,#82bd42 100%);
				width: auto;
				min-width: 58px;
				height: 32px;
			}
	
	.one .list1-edit:hover {
				transform: translate3d(-4px, 0px, 0px);
			}
	
	.one .list1-del {
				border: 1px solid #0260ad30;
				cursor: pointer;
				padding: 0 6px 0 4px;
				margin: 0px 5px 5px 0;
				color: #fff;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
				background: linear-gradient(to bottom, #bc3423 0%,#cd4433 100%);
				width: auto;
				min-width: 58px;
				height: 32px;
			}
	
	.one .list1-del:hover {
				transform: translate3d(-4px, 0px, 0px);
			}
	
	.one .list1-btn8 {
				border: 1px solid #323537;
				cursor: pointer;
				padding: 0 6px 0 4px;
				margin: 0px 5px 5px 0;
				color: #fff;
				font-size: inherit;
				transition: all 0.5s;
				border-radius: 3px;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
				text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.4);
				background: linear-gradient(to bottom, #4b4f51 0%,#414547 100%);
				width: auto;
				min-width: 48px;
				height: 32px;
			}
	
	.one .list1-btn8:hover {
				transform: translate3d(-4px, 0px, 0px);
			}
	
	.main-content .el-table .el-switch {
				display: inline-flex;
				vertical-align: middle;
				line-height: 30px;
				position: relative;
				align-items: center;
				height: 30px;
			}
	.main-content .el-table .el-switch ::v-deep .el-switch__label--left {
				cursor: pointer;
				margin: 0 10px 0 0;
				color: #333;
				font-weight: 500;
				display: inline-block;
				vertical-align: middle;
				font-size: 16px;
				transition: .2s;
				height: 30px;
			}
	.main-content .el-table .el-switch ::v-deep .el-switch__label--right {
				cursor: pointer;
				margin: 0 0 0 10px;
				color: #333;
				font-weight: 500;
				display: inline-block;
				vertical-align: middle;
				font-size: 16px;
				transition: .2s;
				height: 30px;
			}
	.main-content .el-table .el-switch ::v-deep .el-switch__core {
				border: 1px solid #b0d5f6;
				cursor: pointer;
				border-radius: 20px;
				margin: 0;
				outline: 0;
				background: #b0d5f6;
				display: inline-block;
				width: 40px;
				box-sizing: border-box;
				transition: border-color .3s,background-color .3s;
				height: 20px;
			}
	.main-content .el-table .el-switch ::v-deep .el-switch__core::after {
				border-radius: 100%;
				top: 1px;
				left: 1px;
				background: #FFF;
				width: 16px;
				position: absolute;
				transition: all .3s;
				height: 16px;
			}
	.main-content .el-table .el-switch.is-checked ::v-deep .el-switch__core::after {
				margin: 0 0 0 -17px;
				left: 100%;
			}
	
	.main-content .el-table .el-rate ::v-deep .el-rate__item {
				cursor: pointer;
				display: inline-block;
				vertical-align: middle;
				font-size: 0;
				position: relative;
			}
	.main-content .el-table .el-rate ::v-deep .el-rate__item .el-rate__icon {
				margin: 0 3px;
				color: #c0c4cc;
				display: inline-block;
				font-size: 18px;
				position: relative;
				transition: .3s;
			}

</style>
