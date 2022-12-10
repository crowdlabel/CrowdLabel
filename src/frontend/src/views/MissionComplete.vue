<template>
  <div class="all">
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">任务名称</h3>
      </div>
    </div>
    <div class="body">
      <div class="left_nav">
        <ul class="left_nav_list_top">
          <li>
            <a aria-current="page" class="left_nav_list_item left_nav_list_item_active" data-external="true" href="/projects">
              <p class="list_item_title">任务信息</p>
              <img class="down_arrow" src="../assets/down_arrow_active.png" height="20" width="20">
            </a>
          </li>
        </ul>
        <div class="project_description">
          <p class="text_bold">任务简介：</p>
           <p class="text_normal">
            软件工程是一门研究用工程化方法构建和维护有效、实用和高质量的软件的学科。它涉及程序设计语言、数据库、软件开发工具、系统平台、标准、设计件有电子邮件、嵌入式系统、人机界面、办公套件、操作系统、编译器、数据库、游戏等。同时，各个行业几乎都有计算机软件的应用，如工业、农业、银行、航空、政府部门等。这些应用促进了经济和社会的发展，也提高了工作效率和生活效率 。
            <br />软件工程的目标是：在给定成本、进度的前提下，开发出具有适用性、有效性、可修改性、可靠性、可理解性、可维护性、可重用性、可移植性、可追踪性、可互操作性和满足用户需求的软件产品。追求这些目标有助于提高软件产品的质量和开发效率，减少维护的困难。
           </p>
           <div class="placeholder_text"></div>
            <p class="text_bold">任务类型：</p><p class="text_normal">文字任务</p>
            <p class="text_bold"><br />问题数量：</p><p class="text_normal">10</p>
            <p class="text_bold"><br />积分奖励：</p><p class="text_normal">15</p>
            <div class="placeholder_border"></div>
        </div>
      </div>
      <div class="main_body">
        <h3 class="mission_complete">
          任务完成！
        </h3>
        <p class="message">
          恭喜，您已完成了该任务的所有题目！
          <br />您的答题数据已提交，请耐心等待审核，我们会在第一时间将审核结果通过平台消息发送给您。
          <br />您也可以前往 “首页->历史记录” 页面查看自己所有已提交任务的状态。
        </p>
        <img class="trophy" src="../assets/trophy.svg" height="180px" width="180px"/>
        <a href="projects">
          <el-button type="primary">返回任务大厅</el-button>
        </a>
        <el-progress :percentage="percentage" :color="customColor"></el-progress>
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
      percentage: 100,
      customColor: '#5D3BE6',
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

.row {
  display: flex;
  flex-direction: row;
}
.row_center {
  text-align: center;
  margin: 0 auto;
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
    min-width: 300px;
    max-width: 300px;
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
    max-width: 300px;
    min-width: 300px;
    box-shadow: 1.2px 0 0 0 rgb(0 0 0 / 10%);
    box-sizing: border-box;
    flex-direction: column;
    height: calc(100vh - 50px);
    min-height: 600px;
}
.left_nav_list_top {
    box-sizing: border-box;
    list-style-type: none;
    flex: 1;
    flex-direction: column;
    margin: 0;
    padding: 12px;
}
.down_arrow {
  margin-left: 140px;
}
.placeholder_text {
  height: 5px;
}
.placeholder_border {
  height: 20px;
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
.list_item_title {
    padding: 10px;
    font-size: 15px;
}
.project_description {
  text-align: left;
  font-size: 14px;
  padding: 0px 20px;
  border-bottom: 1.2px solid rgba(0,0,0,.1);
}
.text_bold {
  font-weight: bold;
  margin: 0px;
  display: inline;
  align-self: center;
}
.text_normal {
  font-weight: normal;
  margin: 0px;
  line-height: 1.5;
  display:inline;
}

.main_body {
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
    display: flex;
    flex:1;
}
.mission_complete {
  text-align:left;
  font-size: 30px;
  font-weight: bold;
  margin: 0px;
  padding: 50px 50px 30px 50px;
}
.message {
  font-size:17px;
  text-align:left;
  padding: 0px 50px 0px 50px;
  line-height:1.6;
}
.trophy {
  align-self:center;
  margin: 30px 0px 40px 0px;
}

::v-deep .el-button--primary {
  border-color: #5D3BE6;
  background-color: #5D3BE6;
  width: 150px;
  height: 50px;
  font-weight:bold;
  font-size:16px;
  border-radius: 8px;
  align-self:center;
}
::v-deep .el-button--primary:hover{
  background-color: rgba(84,47,238,.7);
  border-color: rgba(84,47,238,.1);
}
::v-deep .el-button--primary:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}
::v-deep .el-progress {
  margin: 25px 0px 10px 0px;
  width: 50% !important;
  align-self:center;
}




</style>