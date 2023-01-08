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
           <p id="task_brief" class="text_normal"></p>
           <!-- div class="placeholder_text"></div> -->
            <p class="text_bold"><br />任务类型：</p><p class="text_normal">{{ task_type }}</p>
            <p class="text_bold"><br />任务标签：</p><p class="text_normal" id="tags"></p>
            <p class="text_bold"><br />问题数量：</p><p class="text_normal">{{ task_question_num }}</p>
            <p class="text_bold"><br />积分奖励：</p><p class="text_normal">{{ task_credit }}</p>
            <div class="placeholder_border"></div>
        </div>
      </div>
      <div class="main_body">
        <div class="instruction">
          <p class="text_bold" id="question_title">问题{{cur_question + 1}}：</p>
          
          <p class="text_normal" id="question_prompt"></p>
        </div>
        <div class="info">
          <p class="text_normal">（将鼠标置于图片之上，长按并拖动鼠标即可画框。可以通过点击已画出的方框对其进行调整。）</p>
        </div>
        <div class="content">
          <img class="question_image" :src=question_image />
          <canvas ref="markCanvas" tabindex='0'></canvas>
        </div>
        <div class="answers">
          <el-button round @click="resetCanvas();">清除画布</el-button>
        </div>
        <div class="footer">
          <el-button id="quit_button" type="primary" v-on:click="quit()" plain>退出答题</el-button>
          <a>
            <el-button id="prev_button" type="primary" :disabled="isFirstQuestion" v-on:click="prevQuestion()">&lt; 上一题</el-button>
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
import { ApiClient } from '@/crowdlabel-api/src';
import { UsersApi } from '@/crowdlabel-api/src';
import { TasksApi } from '@/crowdlabel-api/src';
import { QuestionsApi } from '@/crowdlabel-api/src';
import {draw} from "../utils/draw"; // 矩形绘制方法
export default {
  data() {
    return {
      markList: [],
      user: '',
      client: '',
      task_id: '',
      task_name: '',
      task_type: '',
      task_tags: [],
      task_brief: '',
      task_credit: '',
      task_question_num: '',
      task_map: [],
      question: '',
      question_image: '',
      cur_question: 0,
      question_id: 0,
      prompt: '',
      percentage: 0.00,
      customColor: '#5D3BE6',
      radio: -1,
      choicesGiven: [],
      isFirstQuestion: false
    };
  },
  mounted() {
    this.initCanvas(); // 画布初始化
    let self = this
    let base = this.$root.basePath
    self.task_id = localStorage.getItem('TaskID')
    let apiClient  = new ApiClient(base);
    apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization');
    self.client = apiClient;
    let usersApi = new UsersApi(apiClient);
    self.user = usersApi;
    let tasksApi = new TasksApi(apiClient);
    self.task = tasksApi;
    self.task_map = JSON.parse(localStorage.getItem('QuestionList'))
    self.task_type = localStorage.getItem('TaskType');
    let questionsApi = new QuestionsApi(apiClient);
    self.question = questionsApi;
    self.cur_question = parseInt(localStorage.getItem('QuestionIndex'))
    console.log("QUESTION INDEX: " + self.cur_question);
    self.question_id = self.task_map[this.cur_question];
    let my_username = "";
    // 判断当前是否是第一题，如是则disable“上一题”按钮
    if (self.cur_question == 0)
      self.isFirstQuestion = true;
    self.user.getMeUsersMeGet((error, data, response) => {
      console.log(error, data, response)
      let res = JSON.parse(response['text']);
      my_username = res.username;
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/senderlogin');
        return;
      }
    })
    self.task.getTaskTasksTaskIdGet(self.task_id, (error, data, response) => {
      console.log(error, data, response)
      let res = JSON.parse(response['text'])
      self.task_amount = res.responses_required;
      self.task_brief = res.introduction;
      self.task_name = res.name;
      self.task_tags = eval(res.tags);
      self.task_credit = res.credits;
      self.task_question_num = res.questions.length;
      // 填充任务简介
      if (res.introduction == "")
        document.getElementById("task_brief").innerHTML = "该发布者暂未提供简介";
      else
        document.getElementById("task_brief").innerHTML = self.task_brief;
      // 填充任务标签
      let tags_str = "";
      for (let i = 0; i < self.task_tags.length; i++) {
        tags_str += self.task_tags[i];
        if (i != self.task_tags.length - 1) {
          tags_str += ", ";
        }
      }
      document.getElementById("tags").innerHTML = tags_str;
      // 计算任务进度条
      self.percentage = parseInt((((self.cur_question) / self.task_question_num) * 100).toFixed(0));
      // 判断当前是否是最后一题，如是则将“下一题”按钮更改为“完成任务”按钮
      if (self.cur_question == self.task_question_num - 1) {
        document.getElementById("next_button").innerHTML = "完成任务";
      }

    })
    console.log("QUESTION ID: " + self.question_id)
    console.log("TASK ID: " + self.task_id)
    self.question.getQuestionTasksTaskIdQuestionsQuestionIdGet(self.task_id, self.question_id, (error, data, response) => {
      console.log(error, data, response)
      let res = JSON.parse(response['text']);
      // 填充问题
      self.prompt = res.prompt;
      document.getElementById("question_prompt").innerHTML = self.prompt;
      console.log("PREVIOUS ANSWERS:")
      console.log(res.answers)
      console.log("Original MARKLIST")
      console.log(self.markList)
      // 如已回答过该题，填充答案
      // 如已回答过该题，填充答案
      for (let i = 0; i < res.answers.length; i++) {
        let cur_answer = res.answers[i];
        console.log(cur_answer)
        console.log(cur_answer.answer)
        console.log(cur_answer.respondent)
        if (cur_answer.respondent == my_username) { // 当前用户已回答
          console.log("FOUND")
          for (let i = 0; i < cur_answer.answer.boxes.length; i++) {
          self.markList.push({
            x: cur_answer.answer.boxes[i].top_left.x,
            y: cur_answer.answer.boxes[i].top_left.y,
            w: cur_answer.answer.boxes[i].bottom_right.x - cur_answer.answer.boxes[i].top_left.x,
            h: cur_answer.answer.boxes[i].bottom_right.y - cur_answer.answer.boxes[i].top_left.y
          });
        }
        console.log(self.markList)
        this.initCanvas(); // 画布初始化
        }
      }
      
        
    })
    self.question.getQuestionResourceTasksTaskIdQuestionsQuestionIdResourceGet(self.task_id, self.question_id, (error, data, response) => {
      console.log(error, data, response)
        let binaryData = [];
        binaryData.push(response.body);
        let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
        self.question_image = imageObjectURL;
    })
    self.task.getProgressTasksTaskIdProgressGet(self.task_id, (error, data, response) => {
      console.log(error, data, response)
      let res = JSON.parse(response['text']);
      let progress = res.progress;
      console.log("TASK PROGRESS: " + progress)
    })

    
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
                ctx.strokeStyle = '#5D3BE6'
                cav.style.cursor = 'crosshair'
                
                // 计算使用变量
                let list = this.markList; // 画框数据集合, 用于服务端返回的数据显示和绘制的矩形保存
                // 若服务端保存的为百分比则 此处需计算实际座标, 直接使用实际座标可省略
                /*list.forEach(function (value, index, array) {
                    let newValue = {
                        x: value.x * cav.width,
                        y: value.y * cav.height,
                        w: value.w * cav.width,
                        h: value.h * cav.height,
                    }
                    list.splice(index, 1, newValue)
                })*/
                
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
        let ctx = cav.getContext('2d');
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
    prevQuestion() {
      // 传答案
      if (this.markList.length > 0) {
        let answer_list = [];
          for (let i = 0; i < this.markList.length; i++) {
            let x_0 = this.markList[i].x;
            let y_0 = this.markList[i].y;
            let x_1 = this.markList[i].x + this.markList[i].w;
            let y_1 = this.markList[i].y + this.markList[i].h;
            console.log("x0: " + x_0);
            console.log("x1: " + x_1);
            console.log("y0: " + y_0);
            console.log("y1: " + y_1);
            let answer = {top_left: {x: x_0, y: y_0}, bottom_right: {x: x_1, y: y_1}};
            answer_list.push(answer);
          }
        let answer_dict = { boxes: answer_list };
        console.log(answer_dict);
        this.question.createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut(this.task_id, this.question_id, answer_dict, (error, data, response) => {
          console.log(error, data, response)
          this.$store.commit('changeQuestionIndex', this.cur_question - 1);
          document.location.href = '/question_image_identify';
        })
      }
      else {
        this.$store.commit('changeQuestionIndex', this.cur_question - 1);
        document.location.href = '/question_image_identify';
      }
    },
    nextQuestion() {
      let list = this.markList;
      if (list.length == 0) {
        this.alertMessage();
      } else {
          // 传答案
          let answer_list = [];
          for (let i = 0; i < this.markList.length; i++) {
            let x_0 = this.markList[i].x;
            let y_0 = this.markList[i].y;
            let x_1 = this.markList[i].x + this.markList[i].w;
            let y_1 = this.markList[i].y + this.markList[i].h;
            let answer = {top_left: {x: x_0, y: y_0}, bottom_right: {x: x_1, y: y_1}};
            answer_list.push(answer);
          }
          let answer_dict = { boxes: answer_list };
          this.question.createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut(this.task_id, this.question_id, answer_dict, (error, data, response) => {
            console.log(error, data, response)
            // 判断跳转到什么页面
            if (this.cur_question + 1 == this.task_question_num) { // 最后一题
              // 弹窗
              this.$confirm('确认完成任务？', '完成任务', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'info'
              }).then(() => {
                this.$store.commit('changeQuestionIndex', this.cur_question + 1);
                this.task.completeTasksTaskIdCompletePost(this.task_id, (error, data, response) => {
                  console.log(error, data, response)
                  document.location.href = '/mission_complete';
                });
              }).catch(() => {
              });
            } else {
              this.$store.commit('changeQuestionIndex', this.cur_question + 1);
              document.location.href = '/question_image_identify';
            }
          })
      }
    },
    handleChange(val) {
      console.log(val);
      this.radio = val;
      console.log(this.radio);
    },
    quit() {
        // 弹窗
        this.$confirm('确认退出任务？您的答题记录将被自动保存。', '退出任务', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'info'
        }).then(() => {
          this.$alert('您的答题记录已保存至草稿箱', '退出成功', {
            confirmButtonText: '好的',
            callback: action => {
              // 上传当前题的答案
              if (this.markList.length > 0) { // 已回答
                let answer_list = [];
                for (let i = 0; i < this.markList.length; i++) {
                  let x_0 = this.markList[i].x;
                  let y_0 = this.markList[i].y;
                  let x_1 = this.markList[i].x + this.markList[i].w;
                  let y_1 = this.markList[i].y + this.markList[i].h;
                  let answer = {top_left: {x: x_0, y: y_0}, bottom_right: {x: x_1, y: y_1}};
                  answer_list.push(answer);
                }
                let answer_dict = { boxes: answer_list };
                this.question.createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut(this.task_id, this.question_id, answer_dict, (error, data, response) => {
                  console.log(error, data, response)
                  document.location.href = '/projects';
                })
              } else {
                document.location.href = '/projects';
              }
            }
          });
        }).catch(() => {
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
  padding: 12px 0px 10px 0px;
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
::v-deep .el-button--primary.is-disabled {
  border-color: #5D3BE6;
  background-color: #5D3BE6;
  border-radius: 8px;
  margin-right: 10px;
}
::v-deep .el-button--primary.is-disabled:hover {
  border-color: #5D3BE6;
  background-color: #5D3BE6;
  border-radius: 8px;
  margin-right: 10px;
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