<template>
  <div class="all">
    <div class="top_nav">
      <div class="page_title">
        <h3 class="title">编辑个人信息</h3>
      </div>
    </div>
    <div class="body">
        <div class="main_body">
            <div class="row row_center">
              <img class="profile_pic" src="../assets/image_placeholder.png"/>
              <div class="button_change_profile">
                <el-button type="primary" plain>更换头像</el-button>
              </div>
            </div>
            <div class="row row_center">
              <div class="input">
              <div class="row input_box">
                <p class="field">用户名：</p>
                <el-input placeholder="用户名" v-model="input" clearable>
                </el-input>
              </div>
              <div class="row input_box">
                <p class="field">邮箱：</p>
                <el-input placeholder="邮箱" v-model="input" clearable>
                </el-input>
              </div>
              <div class="row input_box">
                <p class="field">验证码：</p>
                <el-input placeholder="验证码" v-model="input" clearable :disabled="true">
                </el-input>
              </div>
              <div class="row input_box">
                <p class="field">手机号：</p>
                <el-input placeholder="手机号" v-model="input" clearable>
                </el-input>
              </div>
              <div class="row input_box">
                <p class="field">密码：</p>
                <el-input placeholder="密码" v-model="input" clearable show-password>
                </el-input>
              </div>
            </div>
            <div class="button_verify">
              <el-button type="primary">发送验证码</el-button>
            </div>
            </div>
            <div class="button_row">
                <a href="/myaccount">
                  <el-button type="primary" plain>取消</el-button>
                </a>
                <a href="/myaccount">
                  <el-button type="primary">保存</el-button>
                </a>
            </div>
        </div>
        
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
  data() {
    return {
      dialogVisible: false
    };
  },
  methods: {
    chooseType: function () {
      this.dialogVisible = true
    },
    senderType: function (){
      this.$router.push('/senderlogin')
      // axios.get('http://localhost:8002/senderlogin', {params:{
      //           username: this.username
      //           }
      //       }).then((res) => {
      //           console.log(res)
      //           this.$router.push({
      //               name: 'connected',
      //               params: {
      //               username: this.username,
      //               usage: res.data
      //               }
      //           })
      //           })
      //       .catch((error) => {
      //           console.log(error)
      //       })
    },
    receiverType: function () {
      this.$router.push('/receiverlogin')
    }
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
.back_button {
    box-sizing: border-box;
    display: flex;
    align-items: center;
    border-radius: 10px;
    color: rgba(0,0,0,.7);
    cursor: pointer;
    font-size: 16px;
    height: 40px;
    text-decoration: none;
    white-space: nowrap;
    padding: 0px 10px;
}
.back_button:hover {
  background-color: rgba(0,0,0,.06);
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
    display: flex;
    justify-content: center;
    margin-left: 10px;
    margin-right: 20px;
    position: relative;
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

.left_nav {
    max-width: 230px;
    min-width: 230px;
    box-shadow: 1.2px 0 0 0 rgb(0 0 0 / 10%);
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
}
.left_nav_list_top {
    box-sizing: border-box;
    list-style-type: none;
    flex: 1;
    flex-direction: column;
    margin: 0;
    padding: 12px;
    height: calc(100vh - 50px - 132.2px);
    min-height: 135px;
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
    height: calc(100vh - 329.2px);
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
    margin: 5px 0px;
}
.left_nav_list_item:hover {
    background-color: rgba(0,0,0,.06);
}
.left_nav_list_item_active {
    background-color: rgba(84,47,238,.14);
    color: rgba(84,47,238,1);
    pointer-events: none;
}
.left_nav_list_item_active:hover {
    background-color: rgba(0,0,0,.06);
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
    text-align:center;
    padding: 60px 130px;
}

.username{
  vertical-align: middle;
  text-align: left;
  font-size: 22px;
  font-weight: bold;
  color:black;
  margin: 5px 5px 10px 5px;
}
.row {
  display: flex;
  flex-direction: row;
}
.row_center {
  text-align: center;
  margin: 0 auto;
}

.input_box {
  margin-bottom: 15px;
  text-align: right;
  margin-left: auto;
}
.profile_pic {
  height: 130px;
  width: 130px;
  border-radius: 50%;
  text-align:center;
}
.user_info_column {
  align-self: center;
  margin: 0px 50px 10px 50px;
  display: flex;
  flex-direction: column;
}
.user_info_line {
  margin: 3px;
  display: flex;
  flex-direction: column;
}

.button_row {
  text-align: center;
  margin: 0px;
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
  align-self: center;
  margin-left: 30px;
}

.input {
  display: flex;
  flex-direction: column;
  margin: 40px 0px 50px 0px;
}

::v-deep .el-input {
  width: 280px;
}
::v-deep .el-input__inner:focus {
  border-color:#5D3BE6;
}

.field {
  margin: 0px 5px 0px 0px;
  font-size: 14px;
  color: rgba(0,0,0,.8);
  align-self:center;
}

.button_verify {
  margin-left: 20px;
  margin-top: 95px;
}
</style>