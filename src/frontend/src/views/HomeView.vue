<template>
  <div class="homepage">
    <el-container id="main">
      <el-header id="topnav">
        <h2 class="logo">CrowdLabel</h2>
        <p class="chinese_logo">| 众包平台</p>
        <el-button type="primary" @click="chooseType" id="login">注册/登录</el-button>
      </el-header>

      <el-dialog
          :visible.sync="dialogVisible"
          width="50%"
          min-width="800px"
          class="dialogClass"
          border-radius="12px">
          <div class="type_page">
            <div class="type_title">
              <h2 id="you_are">请问您是？</h2>
            </div>
            <div class="type_select">
              <img src="../assets/sender.png" alt="任务发送方" id="image_sender">
              <p class="chinese_type" id="type_or">或</p>
              <img src="../assets/receiver.png" alt="任务接收方" id="image_receiver">
              <p class="chinese_type" id="chinese_sender">任务发送方</p>
              <p class="chinese_type" id="chinese_receiver">任务接收方</p>
              <el-button class="login_btn" id="sender" @click="senderType"></el-button>
              <el-button class="login_btn" id="receiver" @click="receiverType"></el-button>
            </div>
          </div>
        </el-dialog>

      <el-main id="mid">
        <div class="maintop">
          <div class="mainimage"></div>
          <h1 id="front_big">CrowdLabel</h1>
          <el-button type="primary" round @click="chooseType" id="getstarted">开始体验</el-button>
          <div class="smalltriangle">
          </div>
        </div>
      </el-main>
    </el-container>
    <div id="decoration">
      <img src="../assets/triangleleft.png" class="triangle1">
      <img src="../assets/triangleright.png" class="triangle2">
    </div>
    <div class="intro">
      <h1 class="frontinfo">数据标注平台</h1>
      <p class="infotext">支持计算机视觉、语言工程、自然语言处理多类型数据标注，多重审核，高效高质</p>
    </div>

    <div class="info_page">
      <div class="info_page_left">
        <div class="info_page_box" id="brief_intro">
          <h2 class="info_page_h2">平台简介</h2>
          
        </div>
        <div class="info_page_box" id="demonstration">
          <h2 class="info_page_h2">任务示例</h2>
        </div>
      </div>

      <div class="info_page_right">
        <div class="info_page_box" id="team_info">
          <h2 class="info_page_h2">设计团队</h2>

        </div>
      </div>
    </div>

    <div class="footer">
      <div id="team_contact">
        <p>联系方式 | 电话：+86 1xx-xxxx-xxxx</p>
      </div>
      <div id="team_email">
        <p>邮箱：xxxx20@mails.tsinghua.edu.cn</p>
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
    },
    receiverType: function () {
      this.$router.push('/receiverlogin')
    },
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';
*{
  padding: 0px !important;
  margin: 0px !important;
}
div{
  white-space: nowrap;
}
body{
  padding-right: 0px !important;
  margin-top: 0px !important;
  margin-bottom: 0px !important;
  margin-left: 0px !important;
  margin-right: 0px !important;
}
.info_page{
  display: flex;
  height:470px;
}
/* to continue...with info_page */
.info_page_left{  
  position: relative;
  top: 30px;
  height: 440px;
  width:50%;
}
.info_page_right{
  position: relative;
  top: 30px;
  width:50%;
  height:440px;
}
.info_page_box{
  position:relative;
  border-style: solid;
  border-radius: 12px;
  border-color: #391E5C;
}
#brief_intro{
  left:140px;
  width:60%;
  height: 170px;
}
#team_info{
  top: 30px;
  width:60%;
  left: 80px;
  height: 320px;
}
#demonstration{
  width: 60%;
  top: 30px;
  height:200px;
  left:140px;
}

.homepage{
  width:100%;
  height:1220px;
  min-width: 800px;
}
#mid{
  height:480px;
}
#main{
  height:540px;
}
.maintop{
  height: 480px;
  background-size: cover;
  background-color: black;
  min-width:800px;
}
.mainimage{
  position: absolute;
  height:480px;
  width: 90%;
  min-width:800px;
  background-image: url("../assets/crowdlabel_templogo2.jpg");
  background-position: center;
  background-size: cover;
  z-index: 0;
}
.logo{
  width: 150px;
  height: 40px;
  position: relative;
  top: 12px;
  left: 30px;
  font-family: 'Lobster';
  font-size: 28px;
  color:white;
}
#front_big{
  height: 170px;
  width: 600px;
  position: absolute;
  top:120px;
  left: 70px;
  font-family: 'Lobster';
  color: white;
  font-size: 130px;
}
.chinese_logo{
  width:200px;
  height:40px;
  position:relative;
  top: -26px;
  left: 140px;
  color: white;
  font-family: 'YouSheBiaoTiHei';
  font-size: 24px;
}
#login{
  text-align: center;
  width: 120px;
  height: 32px;
  position:relative;
  top: -65px;
  right:20px;
  float:right;
  font-size: 16px;
  color: white;
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}
#getstarted{
  width: 240px;
  height: 50px;
  position: absolute;
  top: 360px;
  left: 120px;
  color: white;
  background-color: #5D3BE6;
  border-color: #5D3BE6;
  font-size: 24px;
}
#topnav{
  width: 100%;
  background-color: #3C1C66;
}
.smalltriangle{
  position:absolute;
  top:490px;
  left:49%;
  height: 0px;
  width: 0px;
  z-index: 1;
  border-top: 25px solid #E5E5E5 !important;
  border-width: 15px;
  border-style:solid;
}
#decoration{
  width: 100%;
  height: 70px;
}
.triangle1{
  position:relative;
  float:left;
  width:50%;
  height:70px;
}
.triangle2{
  position: relative;
  float:right;
  width:50%;
  height:70px;

}
.intro{
  width:100%;
  height: 100px;
}
.frontinfo{
  position:relative;
  top: 0px;
  font-family: 'PangMenZhengDaoBiaoTi';
  font-size: 55px;
}
.infotext{
  position: relative;
  top: 10px;
  font-family: 'SourceHanSansSC';
  font-size: 18px;
}
::v-deep .dialogClass .el-dialog{
  width: 50%;
  min-width: 400px;
  border-radius: 12px;
}
::v-deep .el-dialog__body{
  padding: 0;
}

.sender{
  width:40px;
  height:40px;
  border-color: transparent;
  color: transparent;
}
.receiver{
  width: 40px;
  height: 40px;
  border-color: transparent;
  color: transparent;
}
#image_sender{
  float:left;
  top: 30px;
  left: 30px;
  width: 40%;
  position: absolute;
}
#image_receiver{
  top: 30px;
  right: 30px;
  float:right;
  width: 40%;
  position:absolute;
}
.type_page{
  width: 100%;
  height: 400px;
  position:relative;
  top: 0px;
}
.chinese_type{
  float:left;
  font-family: "PangMenZhengDaoBiaoTi";
  font-size: 22px;
  width:120px;
}
#type_or{
  position: absolute;
  width: 40px;
  top: 40%;
  left:47%;
  font-size: 28px;
}
.type_select{
  width:100%;
  height: 350px;
}
#chinese_sender{
  position:absolute;
  left: 15%;
  top: 340px;
}
#chinese_receiver{
  float: right;
  position: absolute;
  right:15%;
  top: 340px;
}
.login_btn{
  position: relative;
  width: 37%;
  height: 320px;
  background: transparent;
  color: transparent;
  border-color: transparent;
}
::v-deep .el-button:focus, .el-button:hover{
  color:transparent;
  background:transparent;
  border-color:#5D3BE6;
}
#sender{
  position:absolute;
  top: 50px;
  left:5%;
}
#receiver{
  position:absolute;
  top: 50px;
  right:5%;
}
::v-deep .el-dialog{
  min-width: 750px !important;
}
.footer{
  position:relative;
  background-color: #391E5C;
  height:40px;
}
#team_contact{
  float: left;
  margin-top: 5px !important;
  margin-left: 10px !important;
  font-family: 'PangMenZhengDaoBiaoTi';
  font-size: 20px;
  color:white;
  width:40%;
}
#team_email{
  float:right;
  margin-top: 5px !important;
  margin-right: 30px !important;
  font-family: 'PangMenZhengDaoBiaoTi';
  color:white;
  font-size: 20px;
  width:40%;
}

</style>
