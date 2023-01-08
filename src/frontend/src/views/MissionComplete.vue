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
        <h3 class="mission_complete">
          任务完成！
        </h3>
        <p class="message">
          恭喜，您已完成了该任务的所有题目！
          <br />您的积分奖励已到账，可以前往“首页->我的积分“查看。
          <br />您也可以前往 “首页->历史记录” 查看自己所有已提交的任务。
        </p>
        <img class="trophy" src="../assets/trophy.svg"/>
        <div class="footer">
          <a href="projects">
            <el-button type="primary">返回任务大厅</el-button>
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
import { ApiClient } from '@/crowdlabel-api/src';
import { UsersApi } from '@/crowdlabel-api/src';
import { TasksApi } from '@/crowdlabel-api/src';
import { QuestionsApi } from '@/crowdlabel-api/src';
export default {
  data() {
    return {
      percentage: 100,
      customColor: '#5D3BE6',
      user: '',
      client: '',
      task_id: '',
      task_name: '',
      task_type: '',
      task_tags: [],
      task_brief: '',
      task_cover: '',
      task_credit: '',
      task_question_num: '',
      task_map: [],
      cur_question: 0,
      question_id: 0
    };
  },
  mounted() {
    let self = this
    let base = this.$root.basePath
    self.task_id = localStorage.getItem('TaskID')
    var apiClient  = new ApiClient(base);
    apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization');
    self.client = apiClient;
    var usersApi = new UsersApi(apiClient);
    self.user = usersApi;
    var tasksApi = new TasksApi(apiClient);
    self.task = tasksApi;
    self.task_map = JSON.parse(localStorage.getItem('QuestionList'))
    self.task_type = localStorage.getItem('TaskType');
    var questionsApi = new QuestionsApi(apiClient);
    self.question = questionsApi;
    self.cur_question = parseInt(localStorage.getItem('QuestionIndex'))
    console.log("QUESTION INDEX: " + self.cur_question);
    self.question_id = self.task_map[this.cur_question];
    self.task.getTaskTasksTaskIdGet(self.task_id, (error, data, response) => {
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
      var tags_str = "";
      for (var i = 0; i < self.task_tags.length; i++) {
        tags_str += self.task_tags[i];
        if (i != self.task_tags.length - 1) {
          tags_str += ", ";
        }
      }
      document.getElementById("tags").innerHTML = tags_str;
    })
  },
  methods: {
    
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

.all {
  min-width: 1130px;
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
  height: calc(100vh - 500px);
  width: calc(100vh - 500px);
  min-height:150px;
  min-width:150px;
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
  margin: 25px 0px;
  width: 80% !important;
  align-self:center;
}

.footer {
  text-align:center;
  margin-top:auto;
  margin-bottom: 20px;
}



</style>