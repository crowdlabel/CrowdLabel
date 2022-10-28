<template>
  <div class="homepage">
    <el-container id="main">
      <el-header id="topnav">
        <h2 class="logo">CrowdLabel</h2>
        <p class="chinese_logo">| 众包平台</p>
        <el-button type="primary" round id="login">login/register</el-button>
      </el-header>
      <el-main id="mid">
        <img id="main_background" alt="Vue logo" src="../assets/crowdlabel_templogo2.jpg">
      </el-main>
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
  border: 0px !important;
  margin: 0px !important;
}
body{
  margin-top: 0px !important;
  margin-bottom: 0px !important;
  margin-left: 0px !important;
  margin-right: 0px !important;
}
.logo{
  width: 150px;
  height: 40px;
  position: relative;
  top: 12px;
  left: 30px;
  font-family: 'Lobster';
  font-size: 32px;
  color:white;
}
.chinese_logo{
  width:200px;
  height:40px;
  position:relative;
  top: -24px;
  left: 140px;
  color: white;
  font-family: 'YouSheBiaoTiHei';
  font-size: 24px;
}
#login{
  width: 120px;
  height: 28px;
  position:relative;
  top: -63px;
  left: 450px;
  font-size: 16px;
  color: white;
  background-color: #5D3BE6;
}
#topnav{
  background-color: #3C1C66;
}
#main_background{
  width:100%;
  height:450px;
}
</style>