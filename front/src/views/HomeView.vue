<template>
  <div class="homepage">
    <el-container id="main">
      <el-header id="topnav">
        <h2 class="logo">CrowdLabel</h2>
        <p class="chinese_logo">| 众包平台</p>
        <el-button type="primary" round id="login">注册/登录</el-button>
      </el-header>

      <el-main id="mid">
        <div class="maintop">
          <div class="mainimage"></div>
          <h1 id="front_big">CrowdLabel</h1>
          <el-button type="primary" round id="getstarted">开始体验</el-button>
          <div class="smalltriangle">
          </div>
        </div>
        <div class="triangle1"></div>
        <div class="triangle2"></div>
      </el-main>
      <div class="intro">
          <h1 class="frontinfo">数据标注平台</h1>
          <p class="infotext">支持计算机视觉、语言工程、自然语言处理多类型数据标注，多重审核，高效高质</p>
        </div>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  // name: 'HomeView',
  // components: {
  //   // HelloWorld
  // }
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
  margin-top: 0px !important;
  margin-bottom: 0px !important;
  margin-left: 0px !important;
  margin-right: 0px !important;
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
  height: 30%;
}
.frontinfo{
  position:relative;
  top: 80px;
  font-family: 'PangMenZhengDaoBiaoTi';
  font-size: 55px;
}
.infotext{
  position: relative;
  top: 90px;
  font-family: 'SourceHanSansSC';
  font-size: 18px;
}
</style>