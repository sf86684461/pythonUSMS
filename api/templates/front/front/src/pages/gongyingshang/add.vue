<template>
<div :style='{"width":"100%","padding":"30px calc((100% - 1200px)/2) 40px","margin":"0px auto","position":"relative","background":"#fff"}'>
    <el-form
	  :style='{"border":"1px solid #eee","padding":"30px 0","alignItems":"flex-start","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","position":"relative"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="120px"
    >
          <el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="供应商编号" prop="gongyingshangbianhao">
              <el-input v-model="ruleForm.gongyingshangbianhao" placeholder="供应商编号" disabled></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="供应商名称" prop="gongyingshangmingcheng">
            <el-input v-model="ruleForm.gongyingshangmingcheng" 
                placeholder="供应商名称" clearable :disabled=" false  ||ro.gongyingshangmingcheng"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="地址" prop="dizhi">
            <el-input v-model="ruleForm.dizhi" 
                placeholder="地址" clearable :disabled=" false  ||ro.dizhi"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="联系电话" prop="lianxidianhua">
            <el-input v-model="ruleForm.lianxidianhua" 
                placeholder="联系电话" clearable :disabled=" false  ||ro.lianxidianhua"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="负责人姓名" prop="fuzerenxingming">
            <el-input v-model="ruleForm.fuzerenxingming" 
                placeholder="负责人姓名" clearable :disabled=" false  ||ro.fuzerenxingming"></el-input>
          </el-form-item>
          <el-form-item :style='{"width":"100%","padding":"10px","margin":"0 0 10px","background":"none","display":"inline-block"}' label="联系方式" prop="lianxifangshi">
            <el-input v-model="ruleForm.lianxifangshi" 
                placeholder="联系方式" clearable :disabled=" false  ||ro.lianxifangshi"></el-input>
          </el-form-item>

      <el-form-item :style='{"width":"100%","padding":"0","margin":"0","textAlign":"center"}'>
        <el-button :style='{"border":"0px solid #eccc19","cursor":"pointer","padding":"0","margin":"0 20px 0 0","color":"#fff","borderRadius":"20px","background":"linear-gradient(to right,#f67536,#f64d36),#f64d36","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}'  type="primary" @click="onSubmit">提交</el-button>
        <el-button :style='{"border":"1px solid #ccc","cursor":"pointer","padding":"0","margin":"0","outline":"none","color":"#666","borderRadius":"20px","background":"none","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}' @click="back()">返回</el-button>
      </el-form-item>
    </el-form>
</div>
</template>

<script>
  export default {
    data() {
	  let self = this
      return {
        id: '',
        baseUrl: '',
        ro:{
				gongyingshangbianhao : false,
				gongyingshangmingcheng : false,
				dizhi : false,
				lianxidianhua : false,
				fuzerenxingming : false,
				lianxifangshi : false,
        },
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          gongyingshangbianhao: this.getUUID(),
          gongyingshangmingcheng: '',
          dizhi: '',
          lianxidianhua: '',
          fuzerenxingming: '',
          lianxifangshi: '',
        },


        rules: {
          gongyingshangbianhao: [
          ],
          gongyingshangmingcheng: [
            { required: true, message: '供应商名称不能为空', trigger: 'blur' },
          ],
          dizhi: [
          ],
          lianxidianhua: [
          ],
          fuzerenxingming: [
            { required: true, message: '负责人姓名不能为空', trigger: 'blur' },
          ],
          lianxifangshi: [
          ],
        },
		centerType: false,
      };
    },
    computed: {



    },
    components: {
    },
    created() {
		if(this.$route.query.centerType){
			this.centerType = true
		}
	  //this.bg();
      let type = this.$route.query.type ? this.$route.query.type : '';
      this.init(type);
      this.baseUrl = this.$config.baseUrl;
    },
    methods: {
      getMakeZero(s) {
          return s < 10 ? '0' + s : s;
      },
      // 下载
      download(file){
        window.open(`${file}`)
      },
      // 初始化
      init(type) {
        this.type = type;
        if(type=='cross'){
          var obj = JSON.parse(localStorage.getItem('crossObj'));
          for (var o in obj){
            if(o=='gongyingshangbianhao'){
              this.ruleForm.gongyingshangbianhao = obj[o];
              this.ro.gongyingshangbianhao = true;
              continue;
            }
            if(o=='gongyingshangmingcheng'){
              this.ruleForm.gongyingshangmingcheng = obj[o];
              this.ro.gongyingshangmingcheng = true;
              continue;
            }
            if(o=='dizhi'){
              this.ruleForm.dizhi = obj[o];
              this.ro.dizhi = true;
              continue;
            }
            if(o=='lianxidianhua'){
              this.ruleForm.lianxidianhua = obj[o];
              this.ro.lianxidianhua = true;
              continue;
            }
            if(o=='fuzerenxingming'){
              this.ruleForm.fuzerenxingming = obj[o];
              this.ro.fuzerenxingming = true;
              continue;
            }
            if(o=='lianxifangshi'){
              this.ruleForm.lianxifangshi = obj[o];
              this.ro.lianxifangshi = true;
              continue;
            }
          }
        }else if(type=='edit'){
			this.info()
		}
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
          }
        });

		if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
			localStorage.removeItem('raffleType')
			setTimeout(() => {
				this.onSubmit()
			}, 300)
		}
      },

    // 多级联动参数
      // 多级联动参数
      info() {
        this.$http.get(`gongyingshang/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {
			if(this.ruleForm.gongyingshangbianhao){
				this.ruleForm.gongyingshangbianhao = String(this.ruleForm.gongyingshangbianhao)
			}
			//更新跨表属性
			var crossuserid;
			var crossrefid;
			var crossoptnum;
			this.$refs["ruleForm"].validate(valid => {
				if(valid) {
					if(this.type=='cross'){
						var statusColumnName = localStorage.getItem('statusColumnName');
						var statusColumnValue = localStorage.getItem('statusColumnValue');
						if(statusColumnName && statusColumnName!='') {
							var obj = JSON.parse(localStorage.getItem('crossObj'));
							if(!statusColumnName.startsWith("[")) {
								for (var o in obj){
									if(o==statusColumnName){
										obj[o] = statusColumnValue;
									}
								}
								var table = localStorage.getItem('crossTable');
								this.$http.post(table+'/update', obj).then(res => {});
							} else {
								crossuserid=Number(localStorage.getItem('frontUserid'));
								crossrefid=obj['id'];
								crossoptnum=localStorage.getItem('statusColumnName');
								crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
							}
						}
					}
					if(crossrefid && crossuserid) {
						this.ruleForm.crossuserid=crossuserid;
						this.ruleForm.crossrefid=crossrefid;
						var params = {
							page: 1,
							limit: 10,
							crossuserid:crossuserid,
							crossrefid:crossrefid,
						}
						this.$http.get('gongyingshang/list', {
							params: params
						}).then(res => {
							if(res.data.data.total>=crossoptnum) {
								this.$message({
									message: localStorage.getItem('tips'),
									type: 'error',
									duration: 1500,
								});
								return false;
							} else {
								// 跨表计算


								this.$http.post(`gongyingshang/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
									if (res.data.code == 0) {
										this.$message({
											message: '操作成功',
											type: 'success',
											duration: 1500,
											onClose: () => {
												this.$router.go(-1);
											}
										});
									} else {
										this.$message({
											message: res.data.msg,
											type: 'error',
											duration: 1500
										});
									}
								});
							}
						});
					} else {


						this.$http.post(`gongyingshang/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				}
			});
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		// 返回
		back() {
			this.$router.go(-1);
		},
    }
  };
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item ::v-deep  .el-form-item__label {
	  padding: 0 10px 0 0;
	  color: #666;
	  font-weight: 500;
	  width: 120px;
	  font-size: 14px;
	  line-height: 40px;
	  text-align: right;
	}
	
	.add-update-preview .el-form-item ::v-deep  .el-form-item__content {
	  margin-left: 120px;
	}
	
	.add-update-preview .el-input ::v-deep  .el-input__inner {
	  border: 1px solid #ddd;
	  padding: 0 12px;
	  color: #666;
	  font-size: 14px;
	  border-color: #ddd;
	  border-radius: 0px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 250px;
	  height: 40px;
	}
	.add-update-preview .el-input-number ::v-deep  .el-input__inner {
		text-align: left;
	  border: 1px solid #ddd;
	  padding: 0 12px;
	  color: #666;
	  font-size: 14px;
	  border-color: #ddd;
	  border-radius: 0px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  background: none;
	  width: auto;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 250px;
	  height: 40px;
	}
	.add-update-preview .el-input-number ::v-deep  .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number ::v-deep  .el-input-number__increase {
		display: none;
	}
	
	.add-update-preview .el-select ::v-deep  .el-input__inner {
	  border-radius: 0px;
	  padding: 0 10px;
	  color: #666;
	  background: none;
	  width: auto;
	  font-size: 14px;
	  border-color: #ddd;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 250px;
	  height: 40px;
	}
	
	.add-update-preview .el-date-editor ::v-deep  .el-input__inner {
	  border-radius: 0px;
	  padding: 0 10px 0 30px;
	  color: #666;
	  background: none;
	  width: auto;
	  font-size: 14px;
	  border-color: #ddd;
	  border-width: 1px;
	  border-style: solid;
	  min-width: 250px;
	  height: 40px;
	}
	
	.add-update-preview ::v-deep  .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview ::v-deep  .upload .upload-img {
	  cursor: pointer;
	  color: #999;
	  font-size: 24px;
	  border-color: #ddd;
	  line-height: 80px;
	  border-radius: 2px;
	  background: none;
	  width: 100px;
	  border-width: 1px;
	  border-style: solid;
	  text-align: center;
	  min-width: 150px;
	  height: 80px;
	}
	
	.add-update-preview ::v-deep  .el-upload-list .el-upload-list__item {
	  cursor: pointer;
	  color: #999;
	  font-size: 24px;
	  border-color: #ddd;
	  line-height: 80px;
	  border-radius: 2px;
	  background: none;
	  width: 100px;
	  border-width: 1px;
	  border-style: solid;
	  text-align: center;
	  min-width: 150px;
	  height: 80px;
	}
	
	.add-update-preview ::v-deep  .el-upload .el-icon-plus {
	  cursor: pointer;
	  color: #999;
	  font-size: 24px;
	  border-color: #ddd;
	  line-height: 80px;
	  border-radius: 2px;
	  background: none;
	  width: 100px;
	  border-width: 1px;
	  border-style: solid;
	  text-align: center;
	  min-width: 150px;
	  height: 80px;
	}
	
	.add-update-preview .el-textarea ::v-deep  .el-textarea__inner {
	  border: 1px solid #ddd;
	  border-radius: 0px;
	  padding: 12px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  color: #666;
	  background: none;
	  width: 60%;
	  font-size: 14px;
	  height: 120px;
	}
</style>
