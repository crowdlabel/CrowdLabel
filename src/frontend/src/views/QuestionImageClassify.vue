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
        <div class="instruction">
          <p class="text_bold">问题2：</p>
          <p class="text_normal">查看下方图片，并对图片分类。</p>
        </div>
        <img class="image" src="../assets/image_placeholder.png"/>
        <div class="question">
          这是一张什么图片？
        </div>
        <div class="answers">
          <el-radio-group v-model="radio">
            <el-radio :label="1">哺乳动物</el-radio>
            <el-radio :label="2">昆虫</el-radio>
            <el-radio :label="3">鱼类</el-radio>
          </el-radio-group>
        </div>
        <div class="footer">
          <a href="/projects">
            <el-button type="primary" plain>退出答题</el-button>
          </a>
          <a href="/question_text">
            <el-button type="primary">&lt 上一题</el-button>
          </a>
          <a href="/question_image_identify">
            <el-button type="primary">下一题 ></el-button>
          </a>
        </div>
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
      percentage: 40,
      customColor: '#5D3BE6',
      radio: -1
    };
  },
  methods: {
    
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

.all {
  min-width: 1050px;
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
    min-height: 590px;
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
  display:inline;
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

.instruction {
  text-align:left;
  padding: 30px 40px 0px 40px;
}
.image {
  align-self:center;
  border-radius:8px;
  margin:20px 0px 30px 0px;
  height:calc(100vh - 380px);
  width: calc(1.5 * (100vh - 380px));
  min-height: 280px;
  min-width: 420px;
}
.question {
  text-align: left;
  font-size: 18px;
  font-weight: bold;
  padding-left: 45px;
}

::v-deep .el-button--primary {
  border-color: #5D3BE6;
  background-color: #5D3BE6;
  border-radius: 8px;
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
  border-color: #5D3BE6;
  color: #5D3BE6;
  background-color: #fff;
}

::v-deep .el-progress {
  margin: 25px 0px 10px 0px;
  width: 50% !important;
  align-self:center;
}


.answers {
  margin: 10px 0px 20px 0px;
}
::v-deep .el-radio-group {
  transform:scale(1.2);
  font-size:30px !important;
}
::v-deep .el-radio__label {
  color: black;
}
::v-deep .el-radio__input .el-radio__inner {
  border-color: rgba(0, 0, 0, 0.2);
}
/* 选中后radio文本的颜色 */
::v-deep .el-radio__input.is-checked + .el-radio__label {
  color: #5D3BE6;
}
/* radio选中后小圆点的颜色 */
::v-deep .el-radio__input.is-checked .el-radio__inner {
  background: #5D3BE6 !important;
  border-color: #5D3BE6 !important;
}
/* hover时颜色 */
::v-deep .el-radio__inner:hover {
  border-color: #5D3BE6;
}

::v-deep .el-progress {
  margin: 25px 0px;
  width: 80% !important;
  align-self:center;
}

.footer {
  text-align:center;
  margin-top:auto;
}



</style>