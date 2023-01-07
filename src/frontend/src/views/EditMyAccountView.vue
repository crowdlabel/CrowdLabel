<template>
  <div class="all">
    <div class="top_nav">
      <div class="page_title">
        <h3 class="title">编辑个人信息</h3>
      </div>
    </div>
    <div class="body">
        <div class="main_body">
          <div class="user_name">
            <p id="userid"> {{  username }}</p>
          </div>
          <div class="row row_center">
            <img class="profile_pic" :src="mainProfile"/>
            <div class="button_change_profile">
              <el-button type="primary" plain @click="openUploadDialog">更换头像</el-button>
            </div>       
          </div>

          <el-dialog title="上传头像" :visible.sync="UploadProfilePage"
            width="50%"
            min-width="420px"
            class="UploadProfileClass"
            border-radius="12px"
            :before-close="beforeDialogClose">
            <div>
              <el-upload class="upload_file" action="none"
                :headers="{ 'Content-Type': 'multipart/form-data'}"
                accept=".jpg,.jpeg,.png,.JPG,.JPEG"
                ref="Upload"
                :auto-upload="false"
                :on-change="handleChange"
                :limit="1"
                :on-exceed="handleExceed">
                <img :src="piclist" class="avatar">
              </el-upload>
              <p>点击上传</p>
              <el-button type="primary" plain class="fileSelectConfirm" @click="changeProfile">确定</el-button>
            </div>
          </el-dialog>

            <div class="row row_center">
              <el-tabs stretch v-model="activeName" @tab-click="handleTabClick" class="tabs">
                <el-tab-pane label="修改密码" name="changePassword">
                  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                    <el-form-item prop="oldpass">
                      <el-input placeholder="请输入旧密码" type="password" v-model="ruleForm.oldpass" id="oldpassword" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item prop="pass">
                      <el-input placeholder="请输入新密码" type="password" v-model="ruleForm.pass" id="newpassword" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item prop="checkPass">
                      <el-input placeholder="请确认新密码" type="password" v-model="ruleForm.checkPass" id="newpassword2" autocomplete="off"></el-input>
                    </el-form-item>
                  </el-form>
                </el-tab-pane>

                <el-tab-pane label="修改邮箱" name="changeEmail">
                  <el-form :model="emailForm" status-icon :rules="emailrules" ref="emailForm" label-width="100px" class="demo-ruleForm">
                    <el-form-item prop="newemail">
                      <el-input placeholder="请输入邮箱地址" v-model="emailForm.newemail" id="newemail" autocomplete="off"></el-input>
                      </el-form-item>
                    <el-form-item prop="passforemail">
                      <el-input placeholder="请输入密码" type="password" v-model="emailForm.passforemail" id="oldpasswordforemail" autocomplete="off"></el-input>
                      </el-form-item>
                    <el-form-item prop="verif">
                      <div class="verify_code">
                        <el-input placeholder="请输入验证码" autocomplete="off" v-model="emailForm.verif" class="input_verify" id="registerverification"></el-input>
                        <el-button :disabled="disable" type="primary" plain class="button_verify" @click="verifyEmailbtn()">{{text}}</el-button>
                      </div>
                    </el-form-item>
                  </el-form>
                </el-tab-pane>
              </el-tabs>
              
            </div>
            <div class="button_row">
                <el-button type="primary" @click="goBack" plain>取消</el-button>
                <el-button type="primary" @click="editInformation">修改</el-button>
            </div>
        </div>
        
    </div>
  </div>
</template>


<script>
import { ApiClient } from '@/crowdlabel-api/src';
import { UsersApi } from '@/crowdlabel-api/src';
import { AuthApi } from '@/crowdlabel-api/src';

export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
      if (!/^[\x21-\x7e]{8,64}$/.test(value)) {
        callback(new Error('密码格式错误:请输入8-64位密码'));
      }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    var validateEmail = (rule, value, callback) => {
      if (value === '') {
      callback(new Error('请输入邮箱'));
      } else {
        let mailReg = /^([a-zA-Z0-9_-]+(.[a-zA-Z0-9])?)@([a-zA-Z0-9_-]+)((.[a-zA-Z0-9_-]+)+)$/
        if (!mailReg.test(value)){
          callback(new Error('邮箱格式错误'));
        } else {
          this.disable = false;
          let ready_email = document.getElementById('newemail').value;
          this.user.availabilityUsersAvailabilityPut({'email': ready_email},
          (error, data, response) => {
            if (!data['email']){
              callback(new Error('邮箱已被占用'));
              } else {
                this.disable = false;
                callback();
              }
            }
          );
        }
      }
    };
    var validateVerif = (rule, value, callback) => {
      if (value === ''){
        callback(new Error('请输入验证码'))
      } else {
        let veriReg = /^[0-9]{6}$/
        if (!veriReg.test(value)){
            callback(new Error('验证码格式错误'))
        }
        else {
            callback();
        }
      }
    };
    var validatePassForEmail = (rule, value, callback) => {
      if (value===''){
        callback(new Error('请输入密码'))
      } else {
        callback();
      }
    };
    var validateOldPass = (rule, value, callback) => {
      if (value===''){
        callback(new Error('请输入旧密码'))
      } else {
        callback();
      }
    }
    return {
      mainProfile:'',
      UploadProfilePage:false,
      username: '',
      usertype: '',
      text: "发送验证码",
      time: 5,
      timer: null,
      disable: true,
      activeName: 'changePassword',
      client: '',
      auth: '',
      user: '',
      profile: '',
      piclist: [],
      ruleForm: {
        oldpass: '',
        pass: '',
        checkPass: '',
      },
      emailForm: {
        newemail: '',
        passforemail: '',
        verif: '',
      },
      rules: {
        oldpass: [
          { validator: validateOldPass, trigger: 'blur'}
        ],
        pass: [
          { validator: validatePass, trigger: 'blur'}
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
      },
      emailrules: {
        newemail: [
          { validator: validateEmail, trigger: 'change'}
        ],
        passforemail: [
          { validator: validatePassForEmail, trigger: 'blur'}
        ],
        verif: [
          { validator: validateVerif, trigger: 'blur' }
        ]
      }
    };
  },
  created () {
    const time = localStorage.getItem('time');
    if (time && time>0) {
      this.text = time + "s后重新发送"
      this.time = time
      this.verifyEmailbtn();
    }
  },
  mounted() {
    let self = this;
    var apiClient  = new ApiClient('http://localhost:8000');
    apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization')
    self.client = apiClient
    var usersApi = new UsersApi(apiClient);
    self.user = usersApi
    self.user.getMeUsersMeGet((error, data, response) => {
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/');
      }
      let a = JSON.parse(response['text'])
      console.log(a)
      self.username = a.username
      self.usertype = a.user_type
    })
    self.user.getPfpUsersMeProfilePictureGet((error, data, response) => {
      if (response.status == 404){
        self.mainProfile = '../image_placeholder.png'
      } else {
        let binaryData = [];
        binaryData.push(response.body);
        let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
        self.mainProfile = imageObjectURL
        self.piclist = imageObjectURL
      }
    })
  },
  methods: {
    changeProfile () {
      console.log(this.profile)
      this.user.uploadPfpUsersMeProfilePicturePost(this.profile,(error, data, response) => {
        if(response.status == 200){
          this.UploadProfilePage = false;
          let binaryData = [];
          binaryData.push(this.profile);
          let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
          this.mainProfile = imageObjectURL
          this.piclist = imageObjectURL
          this.goBack()
        }
      })
    },
    beforeDialogClose (done) {
      this.piclist = []
      done()
    },
    getFileType(name){
      let startIndex = name.lastIndexOf(".");
      if (startIndex !== -1) {
        return name.slice(startIndex+1).toLowerCase();
      } else {
        return ""; 
      }
    },
    handleExceed(file, fileList){
      this.$set(fileList[0], 'raw', file[0]);
      this.$set(fileList[0], 'name', file[0].name);
      this.$refs['Upload'].clearFiles();//清除文件
      this.$refs['Upload'].handleStart(file[0]);//选择文件后的赋值方法
    },
    handleChange(file, fileList) {
      let self = this;
      if (file.size / (1024*1024)>20) {
        self.$message.warning("当前限制文件大小不能大于20M");
        self.profile = "";
        self.piclist= [];
        return false;
      }
      let suffix = self.getFileType(file.name);
      let suffixArray = ["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"];
      if (suffixArray.indexOf(suffix) === -1) {
        self.$message({
          message: "文件格式错误",
          type: "error",
          duration: 2000
        });
        self.profile = "";
        self.piclist =[];
      }else{
        self.profile = file.raw;
        let binaryData = [];
        binaryData.push(file.raw);
        let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData))
        self.piclist = imageObjectURL;
      }
    },
    openUploadDialog () {
      this.UploadProfilePage = true;
      if(this.piclist == ''){
        this.piclist = '../image_placeholder.png'
      } else{
        this.piclist = this.mainProfile
      }
    },
    handleTabClick(tab, event){
      console.log(tab, event)
    },
    verifyEmailbtn () {
      this.disable=true
      var ready_email = document.getElementById('newemail').value
      console.log(ready_email);
      this.user.verifyEmailUsersVerifyEmailPost({
          "email": ready_email
      });
      this.text = this.time + "s后重新发送"
      localStorage.setItem('time', this.time)
      this.timer = setInterval(() => {
        if (this.time > 0) {
          this.time--
          localStorage.setItem('time', this.time)
          this.text = this.time + "s后重新发送"
        } else {
          clearInterval(this.timer);
          this.time = 5
          this.disable = false
          this.text = '发送验证码'
        }
      }, 1000)
    },
    goBack(){
      if (this.usertype == "respondent"){
        this.$router.push({
          path: '/myaccount',
        })
      } else {
        this.$router.push({
          path: '/senderaccount',
        })
      }
    },
    editInformation(){
      let self = this
      if(self.activeName == "changePassword"){
        var oldpas = document.getElementById("oldpassword").value
        var newpas = document.getElementById("newpassword").value
        self.user.editMeUsersMePatch({
          "old_password": oldpas,
          "new_password": newpas
        }, (error,data, response)=> {
          if(response.status==400){
            this.$confirm("密码错误", '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'info',
            }).then(() => {
              
            }).catch(() => {
              
            });
          }else if(response.status==200){
            alert('成功修改密码');
            goBack();
          }
        });
      } else {
        var newmail = document.getElementById("newemail").value
        var passforemail = document.getElementById("oldpasswordforemail").value
        var verification = document.getElementById("registerverification").value
        console.log(verification)
        self.user.editMeUsersMePatch({
          "new_email": newmail,
          "verification_code": verification,
          "password": passforemail,
        }, (error,data, response)=> {
          if(response.status==400){
            this.$confirm("密码或验证码错误", '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'info',
            }).then(() => {
              
            }).catch(() => {
              
            });
          }else if(response.status==200){
            alert("成功修改邮箱")
            this.goBack()
          }
        });
      }
      
    },
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

.all {
  min-width: 800px;
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
    cursor: pointer;
    display: flex;
    min-width: 230px;
    max-width: 230px;
    padding-left: 10px;
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
    text-align: center;
}

.main_body {
  width: 400px;
  box-sizing: border-box;
  flex-direction: column;
  position: relative;
  display: flex;
  flex:1;
  text-align:center;
  padding: 60px 240px;
}

.row_center {
  text-align: center;
  margin: 0 auto;
}

.profile_pic {
  height: 130px;
  width: 130px;
  border-radius: 50%;
  text-align:center;
}

.button_row {
  text-align: center;
  margin-top: 20px;
}
::v-deep .el-button--primary {
  border-color: #5D3BE6;
  background-color: #5D3BE6;
  margin-right: 10px;
}
::v-deep .el-button--primary:hover{
  background-color: rgba(84,47,238,.7);
  border-color: rgba(84,47,238,.1);
}
::v-deep .el-button--primary:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}

::v-deep .el-button--primary.is-plain {
  border-color: #5D3BE6;
  color: #5D3BE6;
  background-color: #fff;
}
::v-deep .el-button--primary.is-plain:hover{
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}
::v-deep .el-button--primary.is-plain:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}

.button_change_profile {
  margin-top: 10px;
  align-self: center;
}

.input {
  display: flex;
  flex-direction: column;
  margin: 40px 0px 40px 0px;
}

::v-deep .el-input__inner:focus {
  border-color:#5D3BE6;
}

::v-deep .el-form-item {
  margin: 0px !important;
}
::v-deep .el-form-item__error {
  left: 10%;
}

::v-deep .el-form-item__content{
  margin-left:0px !important;
  margin-bottom: 0px !important;
  width:100%;
  line-height: 0px;
}

::v-deep .el-form-item.el-form-item--feedback{
  display: flex;
  /*margin-bottom: 18px !important;*/
}

::v-deep .input_verify{
  width: 55% !important;
  float: left;
}

::v-deep .button_verify{
  width:40% !important;
  float: right;
}

::v-deep .el-tabs__header{
  margin-left:auto;
  margin-right:auto;
  width:70%;
  margin-bottom:30px;
}
::v-deep .el-tabs__active-bar{
  background-color:#6729B6;
}
::v-deep .el-tabs__item:hover{
  color: #6729B6;
}
::v-deep .el-tabs__item.is-active{
  color:#6729B6;
}

::v-deep .el-form-item.el-form-item--feedback{
  display: flex;
  margin-bottom: 18px !important;
}

::v-deep .el-tabs__content{
  padding-left:20px;
  padding-right:20px;
}

.user_name{
  height:40px;
}

.tabs{
  margin-top: 20px;
}

#userid{
  margin-top:0px;
  font-size: 30px;
}

.profile_preview{
  height:200px;
  width:200px;
  border-radius: 50%;
}

.fileSelectConfirm{
  margin-top:20px;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>