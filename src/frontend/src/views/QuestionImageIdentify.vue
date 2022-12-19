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
          <p class="text_bold">问题3：</p>
          <p class="text_normal">查看下方图片，用鼠标框出所有</p>
          <p class="text_bold">行人。</p>
        </div>
        <div class="info">
          <p class="text_normal">（将鼠标置于图片之上，长按并拖动鼠标即可画框。可以通过点击已画出的方框对其进行调整。）</p>
        </div>
        <div class="content">
          <!-- <img class="img_content" src="../assets/people.png" /> -->
          <canvas ref="markCanvas" tabindex='0'></canvas>
        </div>
        <div class="answers">
          <el-button round @click="resetCanvas();">清除画布</el-button>
        </div>
        <div class="footer">
          <el-button id="quit_button" type="primary" v-on:click="quit()" plain>退出答题</el-button>
          <a href="/question_image_classify">
            <el-button type="primary">&lt 上一题</el-button>
          </a>
          <el-button id="next_button" type="primary" v-on:click="nextQuestion()">下一题 ></el-button>
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
import {draw} from "../utils/draw"; // 矩形绘制方法
export default {
  data() {
    return {
      percentage: 60,
      customColor: '#5D3BE6',
      markList: [],
      choicesGiven: [
        { label: "哺乳动物", value: 0 },
        { label: "昆虫", value: 1 },
        { label: "鱼类", value: 2}
      ]
    };
  },
  mounted() {
    this.initCanvas(); // 画布初始化
  },
  methods: {
    /* 画布初始化 */
    initCanvas() {
            // let that = this
            this.$nextTick(() => {
                // 初始化canvas宽高
                let cav = this.$refs.markCanvas;
                cav.width = '520';
                cav.height = '390';
                let ctx = cav.getContext('2d');
                ctx.strokeStyle = 'blue'
                cav.style.cursor = 'crosshair'
                
                // 计算使用变量
                let list = this.markList; // 画框数据集合, 用于服务端返回的数据显示和绘制的矩形保存
                // 若服务端保存的为百分比则 此处需计算实际座标, 直接使用实际座标可省略
                list.forEach(function (value, index, array) {
                    let newValue = {
                        x: value.x * cav.width,
                        y: value.y * cav.height,
                        w: value.w * cav.width,
                        h: value.h * cav.height,
                    }
                    list.splice(index, 1, newValue)
                })
                
                // 若list长度不为0, 则显示已标记框
                if (list.length !== 0) {
                    list.forEach(function (value, index, array) {
                        // 遍历绘制所有标记框
                        ctx.rect(value.x, value.y, value.w, value.h);
                        ctx.stroke();
                    });
                }
                
                // 调用封装的绘制方法
                draw(cav,list);
 
                // 备注: js中对象操作指向的是对象的物理地址, 获取绘制完矩形的结果数组直接取用或处理this.markList即可
            })
        },
      resetCanvas () {
        // 标注的信息都放在这个数组中
        let cav = this.$refs.markCanvas;
        this.markList = [];
        // history = [history[0]]
        var ctx = cav.getContext('2d');
        ctx.clearRect(0, 0, cav.width, cav.height);
        this.initCanvas(); // 画布初始化
        // addHistoy(history, ctx, mycanvas)
      },
    alertMessage() {
        this.$message({
          showClose: true,
          message: '您尚未作答本题目，请先完成本题。',
          type: 'warning'
        });
    },
    nextQuestion() {
      let list = this.markList;
      if (list.length == 0) {
        this.alertMessage();
      } else {
        document.location.href = '/question_audio';
      }
    },
    handleChange(val) {
      console.log(val);
      this.radio = val;
      console.log(this.radio);
    },
    quit() {
        this.$confirm('是否要保存当前的答题进度?', '退出任务', {
          confirmButtonText: '是',
          cancelButtonText: '否',
          type: 'warning'
        }).then(() => {
          /*
          this.$message({
            type: 'success',
            message: '保存成功!'
          });
          */
          document.location.href = '/projects';
        }).catch(() => {
          /*
          this.$message({
            type: 'info',
            message: '已取消保存'
          });  
          */     
          document.location.href = '/projects';   
        });
      }
  }
}
</script>

<style lang='scss' scoped>
@import '@/assets/font/font.css';

.content {
    position: relative;
    align-self: center;
    // transform: translateX(-50%) translateX(-50%);
    width: 520px;
    height: 390px;
    
    img {
        position: absolute;
        // top: 20px;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 9;
    }
 
    canvas {
        position: absolute;
        // top: 20px;
        left: 0;
        z-index: 10;
    }
}

.all {
  min-width: 1150px;
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
    box-shadow: 1.2px 0 0 0 rgba(0,0,0,.1);
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
    box-shadow: 1.2px 0 0 0 rgba(0,0,0,.1);
    box-sizing: border-box;
    flex-direction: column;
    height: calc(100vh - 50px);
    min-height: 652px;
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

.info {
  text-align:center;
  font-size:14px;
  color: rgba(0,0,0,1);
  padding: 12px 0px 5px 0px;
}
.image {
  align-self:center;
  margin:20px 0px 30px 0px;
}
.answers {
  margin: 15px 0px 15px 0px;
}
.question {
  text-align: left;
  font-size: 18px;
  font-weight: bold;
  padding-left: 40px;

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
  margin: 25px 0px;
  width: 80% !important;
  align-self:center;
}

::v-deep .el-button--default.is-round {
  margin: 0px 0px 0px 10px;
  height: 33px;
  border-width: 0.5px;
  padding: 0px 0px !important;
  border-color: #5D3BE6;
  color:#5D3BE6;
  font-size: 13px;
  min-width: 80px;
}
::v-deep .el-button--default.is-round:hover{
  background-color: #5D3BE6;
  border-width: 0.5px;
  color: #fff;
}

::v-deep .el-button--default.is-round:focus {
  background-color: #fff;
  border-width: 0.5px;
  color: #5D3BE6;
}

.footer {
  text-align:center;
  margin-top:auto;
}

</style>