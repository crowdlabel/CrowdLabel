<template>
  <div class="all">
    <div class="top_nav">
      <div class="page_title">
        <h3 class="title">任务详情</h3>
      </div>
    </div>
    <div class="body">
        <div class="main_body">
          <div class="row">
            <div class="title_placeholder"></div>
            <h1 class="project_title">任务名称</h1>
          </div>
          <div class="row project_details">
            <img class="preview_img" src="../assets/image_placeholder.png" height="320" width="450"/>
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
            </div>
          </div>
          <div class="row row_margin">
            <a href="/projects">
              <el-button type="primary" plain>&lt 返回</el-button>
            </a>
            <div class="button_placeholder"></div>
            <a href="/question_text">
              <el-button type="primary">开始答题 > </el-button>
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
  min-width: 1200px;
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

.main_body {
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
    display: flex;
    flex:1;
    text-align:center;
    padding: 60px 100px;
}
.title_placeholder {
  width: 450px;
}
.project_title {
  font-size: 27px;
  font-weight: bold;
  margin-left: 30px;
  margin-bottom: 30px;
}
.project_details {
  text-align: left;
}
.preview_img {
  border-radius: 7px 7px 7px 7px;
}
.project_description {
  margin-left: 30px;
}
.text_bold {
  font-weight: bold;
  margin: 0px;
  display:inline;
}
.text_normal {
  font-weight: normal;
  margin: 0px;
  line-height: 1.5;
  display:inline;
}
.placeholder_text {
  height: 8px;
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
.row_margin {
  margin-top: 45px;
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
  font-size: 15px;
  border-radius: 10px;
  height: 45px;
  font-weight: bold;
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
  margin-left: 365px;
}
::v-deep .el-button--primary.is-plain:hover{
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}
::v-deep .el-button--primary.is-plain:focus {
  border-color: #5D3BE6;
  color: #5D3BE6;
  background-color: #fff;
}
.button_placeholder {
  width: 30px;
}
</style>