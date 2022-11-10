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
          :before-close="handleClose"
          width="50%"
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
      <div class="triangle1"></div>
      <div class="triangle2"></div>
    </div>
    <div class="intro">
      <h1 class="frontinfo">数据标注平台</h1>
      <p class="infotext">支持计算机视觉、语言工程、自然语言处理多类型数据标注，多重审核，高效高质</p>
    </div>

    <div class="info_page">
      <div id="brief_intro">

      </div>
      <div id="demonstration">

      </div>
      <div id="team_info">

      </div>
    </div>
    <div class="footer">

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
.homepage{
  width:100%;
  height:1220px;
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
}
.mainimage{
  position: absolute;
  left: 10%;
  height:480px;
  width: 90%;
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
  position:absolute;
  top:540px;
  left:0%;
  height: 0px;
  width: 0px;
  z-index: 1;
  border-top: 70px solid #D0B4F5 !important;
  border-right: solid transparent;
  border-right-width: 770px;
}
.triangle2{
  position:absolute;
  top:540px;
  right:0%;
  height: 0px;
  width: 0px;
  z-index: 1;
  border-top: 70px solid #D0B4F5 !important;
  border-left: solid transparent;
  border-left-width: 770px;
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
  height: 21vw;
  background: transparent;
  color: transparent;
  border-color: transparent;
}
::v-deep .el-button:focus, .el-button:hover{
  color:transparent;
  background:transparent;
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
</style>