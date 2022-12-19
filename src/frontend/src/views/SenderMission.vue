<template>
  <div>
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">任务大厅</h3>
        <img src="../assets/notifications.svg" alt="label" height="24">
      </div>
      <div class="my_account">
        <img src="../assets/my_account.svg" alt="label" height="23">
      </div>
    </div>
    <div class="body">
        <div class="left_nav">
            <ul class="left_nav_list_top">
                <li>
                    <a aria-current="page" class="left_nav_list_item left_nav_list_item_active" data-external="true" href="/sendermission">
                        <img src="../assets/folder_active.png" height="21" width="20">
                        <p class="list_item_title">我的任务</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/sendercredits">
                        <img src="../assets/credits.png" height="19" width="20">
                        <p class="list_item_title">我的积分</p>
                    </a>
                </li>
                <li tag="li" class="left_nav_spacer">
                </li>
            </ul>
            <ul class="left_nav_list_bottom">
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/settings">
                        <img src="../assets/settings.png" height="20" width="20">
                        <p class="list_item_title">设置</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/about_us">
                        <img src="../assets/about.png" height="20" width="20">
                        <p class="list_item_title">关于我们</p>
                    </a>
                </li>
            </ul>
        </div>

        <el-dialog
          :visible.sync="dialogVisible"
          width="50%"
          min-width="800px"
          class="dialogClass"
          border-radius="12px">
          <div class="type_page">
            <div class="create_h2">
              <h2 id="create_title">创建您新任务</h2>
            </div>
            <div class="create_main">
              <el-form label-width="80px" ref="form" :model="form" :rules="rules">
                <el-form-item prop="name" class="name_item" required>
                  <el-input placeholder="请输入任务名称"  class="mission_name" v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="任务简介:" class="mission_brief" prop="brief" required>
                  <el-input type="textarea" v-model="form.brief" class="brief_input"></el-input>
                </el-form-item>
                <el-form-item label="任务详情:" class="mission_details" prop="details" required>
                  <el-input type="textarea" v-model="form.details" class="details_input"></el-input>
                </el-form-item>
                <el-form-item label="上传封面:" class="mission_file" required>
                  <el-upload class="upload_file" action="none"
                    :headers="{ 'Content-Type': 'multipart/form-data'}"
                    accept=".jpg, .png"
                    :auto-upload="false"
                    :on-change="handleChange"
                    :limit="1"
                    :file-list="form.cover"
                    >
                    <el-button type="primary" size="small" class="click_upload_btn">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传JPG和PNG文件</div>
                  </el-upload>
                </el-form-item>
                <el-form-item label="上传文件:" class="mission_file" required>
                  <el-upload class="upload_file" action="none"
                    :headers="{ 'Content-Type': 'multipart/form-data'}"
                    accept=".zip, .rar"
                    :auto-upload="false"
                    :on-change="handleZip"
                    :limit="1"
                    :file-list="form.zipfile"
                    >
                    <el-button type="primary" size="small" class="click_upload_btn">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传zip或rar文件</div>
                  </el-upload>
                </el-form-item>
                <el-form-item prop="amount" label="任务份额:" required class="mission_credits">
                  <el-input placeholder="请输入任务总份数"  class="credits_input" v-model="form.amount"></el-input>
                </el-form-item>
                <el-form-item prop="credits_each" label="积分奖励:" required class="mission_credits">
                  <el-input placeholder="请输入每份任务报酬积分"  class="credits_input" v-model="form.credits_each"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" class="create_now" @click="create_new_project">立即创建</el-button>
                  <el-button type="default" class="cancel" @click="backToMission">取消</el-button>
                </el-form-item>
              </el-form>
            </div>
          </div>
        </el-dialog>

        <div class="main_body">
            <div class="search_bar">
                <el-input placeholder="搜索任务"></el-input>
                <el-button type="primary" icon="el-icon-search"></el-button>
            </div>
            <div class="filter">
              <p class="title_filter">筛选：</p>
              <el-button-group>
                <el-button round>全部</el-button>
                <el-button round>文字任务</el-button>
                <el-button round>图像任务</el-button>
                <el-button round>视频任务</el-button>
                <el-button round>音频任务</el-button>
              </el-button-group>
            </div>
            <el-button type="primary" round @click="createProject" id="create">创建任务</el-button>
            <div class="display_projects">
              <div class="display_items">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
              </div>
              <div class="display_items">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
              </div>
              <div class="display_items">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
              </div>
              <div class="display_items">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
              </div>
              <div class="display_items">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
              </div>
              <!-- <div class="display_projects_row">
                <div class="project">
                  <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
                </div>
                <div class="project">
                  <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
                </div>
                <div class="project">
                  <el-card :body-style="{ padding: '0px' }">
                    <img src="../assets/image_placeholder.png" class="project_image">
                    <div style="padding: 0px;">
                      <p class="project_title">任务标题</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
                </div>
              </div> -->
            </div>

            <div class="pagination">
              <el-pagination
                background
                layout="prev, pager, next"
                 :total=100>
              </el-pagination>
            </div>
        </div>
    </div>
  </div>
</template>
  
  
<script>
import axios from 'axios'
export default {
  data() {
    // page_num = 5;
    var validateName = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务名称'))
      } else {
        callback();
      }
    };
    var validateBrief = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务简介'))
      } else {
        callback();
      }
    };
    var validateDetails = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务详情'))
      } else {
        callback();
      }
    };
    var validateCreditsEach = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入每份任务积分奖励'))
      } else {
        callback();
      }
    };
    var validateAmount = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务总份数'))
      } else {
        callback();
      }
    };
    return {
      dialogVisible: false,
      // 
      userid: this.$route.query.userid,
      usercredits: 50,
      // 
      multipartFile: [],
      form: {
        name: '',
        brief: '',
        details: '',
        credits_each: '',
        amount: '',
        cover: [],
        zipfile: []
      },
      rules: {
        name: [
          { validator: validateName, trigger: 'blur'}
        ],
        brief: [
          { validator: validateBrief, trigger: 'blur'}
        ],
        details: [
          { validator: validateDetails, trigger: 'blur'}
        ],
        credits_each: [
          { validator: validateCreditsEach, trigger: 'blur'}
        ],
        amount: [
          { validator: validateAmount, trigger: 'blur'}
        ],
      },
    }
  },
  methods: {
    handleChange(file, fileList) {
      let self = this;
      if (file.size / (1024*1024)>1) {
        self.$message.warning("当前限制文件大小不能大于1M");
        self.file = '';
        self.form.cover= [];
        return false;
      }
      let suffix = self.getFileType(file.name);
      let suffixArray = ["jpg", "jpeg", "png"];
      if (suffixArray.indexOf(suffix) === -1) {
        self.$message({
          message: "文件格式错误",
          type: "error",
          duration: 2000
        });
        self.file = "";
        self.form.cover=[];
      }else{
        self.multipartFile.append("cover", file.raw)
        self.file = file.raw;
        self.form.cover = fileList;
      }
    },
    handleZip(file, fileList) {
      let self = this;
      if (file.size / (1024*1024)>20) {
        self.$message.warning("当前限制文件大小不能大于20M");
        self.file = '';
        self.form.zipfile= [];
        return false;
      }
      let suffix = self.getFileType(file.name);
      let suffixArray = ["zip", "rar"];
      if (suffixArray.indexOf(suffix) === -1) {
        self.$message({
          message: "文件格式错误",
          type: "error",
          duration: 2000
        });
        self.file = "";
        self.form.zipfile=[];
      }else{
        self.multipartFile.append("file", file.raw)
        self.file = file.raw;
        self.form.zipfile = fileList;
      }
    },
    getFileType(name){
      let startIndex = name.lastIndexOf(".");
      if (startIndex !== -1) {
        return name.slice(startIndex+1).toLowerCase();
      } else {
        return ""; 
      }
    },
    backToMission() {
      this.dialogVisible = false;
    },
    createProject () {
      this.dialogVisible = true;
    },
    create_new_project () {
      this.multipartFile.append('username', this.userid);
      this.multipartFile.append('missionname', this.form.name);
      this.multipartFile.append('missionamount', this.form.amount);
      this.multipartFile.append('missioncredits', this.form.credits_each)
      this.multipartFile.append('missionbrief', this.form.brief);
      this.multipartFile.append('missiondetails', this.form.details);
      // axios post to create mission
    },
  },
  create() {
    this.multipartFile = new FormData();
  }

}
</script>
  
<style scoped>
@import '@/assets/font/font.css';

::v-deep .dialogClass .el-dialog{
  width: 50% !important;
  min-width: 700px;
  border-radius: 12px;
}
::v-deep .el-dialog__body{
  padding: 0;
}

.top_nav {
  background-color: #fff;
  border-bottom: 1.2px solid rgba(0,0,0,.1);
  box-sizing: border-box;
  display: flex;
  height: 50px;
  position: sticky;
  top: 0;
  z-index: 1000;
}
.top_nav_trigger {
  align-items: center;
  box-shadow: 1.2px 0 0 0 rgb(0 0 0 / 10%);
  box-sizing: border-box;

  display: flex;
  min-width: 230px;
  max-width: 230px;
  padding-left: 20px;
}
.page_title {
  align-items: center;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  padding-left: 20px;
  min-width: 120px;
  flex: 1;
}
.my_account {
  align-items: center;
  align-self: center;
  cursor: pointer;
  display: flex;
  justify-content: center;
  margin-left: 10px;
  margin-right: 20px;
  position: relative;
}
.logo{
  vertical-align: middle;
  text-align: left;
  font-family: 'Lobster';
  font-size: 22px;
  color:black;
  padding: 8px;
}
.title{
  vertical-align: middle;
  text-align: left;
  font-size: 16px;
  font-weight: bold;
  color:black;
}
.body{
    display: flex;
    flex: 1;
    flex-direction: row;
    min-height: 100%;
    min-width: 100%;
}

.left_nav {
    max-width: 230px;
    min-width: 230px;
    box-shadow: 1.2px 0 0 0 rgb(0 0 0 / 10%);
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
    display: flex;
    flex:1;
    justify-content: space-between;
    height: 100%;
}
.left_nav_list_top {
    box-sizing: border-box;
    list-style-type: none;
    flex: 1;
    flex-direction: column;
    margin: 0;
    padding: 12px;
}
.left_nav_list_bottom {
    box-sizing: border-box;
    list-style-type: none;
    border-top: 1.2px solid rgba(0,0,0,.1);
    flex: 1;
    flex-direction: column;
    position: relative;
    bottom: 0;
    margin: 0;
    padding: 12px;
}
.left_nav_spacer {
    height: calc(100vh - 289.2px);
    flex: 1;
}
.left_nav_list_item {
    box-sizing: border-box;
    display: flex;
    align-items: center;
    border-radius: 10px;
    color: rgba(0,0,0,.6);
    cursor: pointer;
    font-size: 16px;
    height: 46px;
    padding: 0 13px;
    text-decoration: none;
    white-space: nowrap;
}
.left_nav_list_item_active {
    background-color: rgba(84,47,238,.14);
    color: rgba(84,47,238,1);
}
.list_item_title {
    padding: 15px;
    font-size: 15px;
}

.main_body {
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
    display: flex;
    flex:1;
    height: calc(100vh - 50px);
    min-width: 1000px;
}

.search_bar {
  flex-direction: row;
  display: flex;
  margin-top:40px;
}

::v-deep .el-input {
  width: 75% !important;
  margin-left: 100px;
}

::v-deep .el-input__inner { 
  font-size: 15px;
  min-width: 400px;
  height: 50px;
  border-radius: 0px;
  margin-top: 20px;
  margin-right: 0px;
}

::v-deep .el-input__inner:focus { 
  border-radius: 0px;
  border-color: #5D3BE6;
}

::v-deep .el-button--primary {
  margin-top: 20px;
  margin-right: 80px;
  padding: 0px 20px;
  border-width: 0px;
  border-radius: 0px 4px 4px 0px;
  background-color: #5D3BE6;
  border-color: #5D3BE6;
  font-size: 20px;
  min-width: 80px;
}

::v-deep .el-button--primary:hover{
  background-color: rgba(84,47,238,.8);
  border-color: #5D3BE6;
}

::v-deep .el-button--primary:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}
::v-deep .el-button.el-button--default:focus, .el-button.el-button--default:hover{
    color: #5D3BE6;
    background-color: #F3EAFF;
}

.filter {
  flex-direction: row;
  display: flex;
  align-items:center;
  margin: 20px 100px 0px 100px;
}
.title_filter {
  padding: 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}
::v-deep .el-button--success {
  margin: 0px 0px 0px 10px;
  height: 30px;
  padding: 0px 0px !important;
  border-width: 0.5px;
  background-color: #5D3BE6;
  border-color: #5D3BE6;
  font-size: 12.5px;
  min-width: 80px;
}
::v-deep .el-button--success:hover{
  background-color: #5D3BE6;
}

::v-deep .el-button--success:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}

::v-deep .el-button--default.is-round {
  margin: 0px 0px 0px 10px;
  height: 30px;
  border-width: 0.5px;
  padding: 0px 0px !important;
  border-color: #5D3BE6;
  color:#5D3BE6;
  font-size: 12.5px;
  min-width: 80px;
}
::v-deep .el-button--default.is-round:hover{
  background-color: #5D3BE6;
  border-width: 0.5px;
  color: #fff;
}

::v-deep .el-button--default.is-round:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
  border-width: 0.5px;
  color: #fff;
}

.order_by {
  flex-direction: row;
  display: flex;
  align-items:center;
  margin: 0px 100px 0px 100px;
}
.title_order_by {
  padding: 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}

.display_projects {
  flex-direction: column;
  display: flex;
  align-items:center;
  margin: 20px 100px;
  margin-bottom:40px;
  cursor: pointer;
  flex-wrap: wrap;
  width: 100%;
  height: 360px !important;
}

.display_items{
  width: 33.3333%;
  height:180px;
  display: flex;
  flex-direction: center;
  align-items: center;
  box-sizing: border-box;
}

.display_projects_row {
  width: 100%;
  flex-direction: row;
  display: flex;
  margin: 15px 0px;
}


.project {
  margin: 0px 30px;
}

::v-deep .el-pagination {
  margin-top: 10px !important;
  margin-bottom: 20px;
}
::v-deep .el-pagination.is-background .el-pager li.active {
  background-color: #5D3BE6 !important;
}
::v-deep .el-pagination.is-background .el-pager li.active:hover {
  color: #fff !important;
}
::v-deep .el-pagination.is-background .el-pager li:hover {
  background-color: #5D3BE6 !important;
  color: #fff !important;
}

.project_title {
  text-align: left;
  margin: 0px 9px 8px 9px;
  font-size: 13px;
}
.project_image {
  height: 130px;
  width: 250px;
}

#create{
  position: absolute;
  float: left; 
  top: 120px;
  left: 800px;
  font-size: 16px;
  padding: 12px 24px;
}

.mission_name{
  float: left;
  margin-left:0px !important;
  margin-top: 0px !important;
  width: 90% !important;
}
::v-deep .el-form-item__content{
  margin-left: 20px !important;
}

::v-deep .el-form-item{
  margin-bottom: 20px;
}

#create_title{
  margin-top:0px;
  margin-bottom:0px !important;
}

.create_now{
  font-size: 16px !important;
  margin-top: 0px !important;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 30px !important;
  border-radius: 10px !important;
}

.cancel{
  font-size: 16px;
  padding-top: 10px !important;
  padding-bottom: 10px !important;
  margin-bottom: 30px !important;
}

.mission_type{
  margin-left: 30px !important;
  margin-right: 30px !important;
}
.mission_file{
  margin-left: 30px !important;
  margin-right: 30px !important;
}

.upload_file{
  float: left;
  width: 80%;
}

::v-deep .el-form-item__label{
  width: 100px !important;
}

.click_upload_btn{
  position: relative !important;
  width: 70px;
  border-radius: 8px !important;
  float:left;
  margin-top: 0px;
  font-size:12px;
  padding: 8px 2px;

}

::v-deep .el-upload__tip{
  float:left;
  position: relative;
  width: 140px;
  line-height: 25px;
}

::v-deep .el-radio-group{
  position: relative;
  float: left;
  top: 14px !important;
}
.mission_name{
  font-size: 14px !important;
  /* height: 36px !important; */
  line-height:30px !important;
}

::v-deep .el-form-item__label{
  position: relative;
  float: left !important;;
}

.mission_brief{
  margin-left: 30px;
  margin-right: 30px;
}

.mission_details{
  margin-left: 30px;
  margin-right: 30px;
}

::v-deep .el-textarea{
  width:80% !important;
  min-height: 40px !important;
  left: -20px;
}

::v-deep .el-upload-list{
  float: left;
  width: 40%;
}

::v-deep .el-upload{
  position: relative !important;
  top: 7px;
  float: left !important;
  width: 80px;
}

.mission_credits{
  margin-left: 30px;
  margin-right: 30px;
}

.credits_input{
  position: relative;
  float: left;
  margin-left:0px !important;
  height: 40px !important;
}

::v-deep .credits_input .el-input__inner{
  margin-top: 0px;
  height:40px;
  font-size: 12px;
}

.name_item{
  margin-left:30px;
  margin-right:30px;
}




</style>