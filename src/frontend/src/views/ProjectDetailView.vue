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
            <h1 class="project_title">{{task_name}}</h1>
          </div>
          <div class="row project_details">
            <img class="preview_img" :src=task_cover height="320" width="450"/>
            <div class="project_description">
              <p class="text_bold">任务简介：</p>
              <p class="text_normal" id="task_brief"></p>
              <p class="text_bold"><br />任务类型：</p><p class="text_normal">{{task_type}}</p>
              <p class="text_bold"><br />任务标签：</p><p class="text_normal" id="tags"></p>
              <p class="text_bold"><br />问题数量：</p><p class="text_normal">{{task_question_num}}</p>
              <p class="text_bold"><br />积分奖励：</p><p class="text_normal">{{task_credit}}</p>
            </div>
          </div>
          <div class="row row_margin">
            <a href="/projects">
              <el-button type="primary" plain>&lt 返回</el-button>
            </a>
            <div class="button_placeholder"></div>
            <el-button id="claim_button" type="primary" v-on:click="claim_task()" :disabled="claim">接受任务</el-button>
            <el-button id="start_button" type="primary" v-on:click="start_task()" :disabled="answer">开始答题 > </el-button>
          </div>
        </div>
        
    </div>
  </div>
</template>


<script>
import { ApiClient } from '@/crowdlabel-api/src';
import { UsersApi } from '@/crowdlabel-api/src';
import { TasksApi } from '@/crowdlabel-api/src';

export default {
  data() {
    return {
      answer: true,
      claim: false,
      client: '',
      user: '',
      task: '',
      task_id: '',
      task_name: '',
      task_type: '',
      task_tags: [],
      task_brief: '',
      task_cover: '',
      task_credit: '',
      task_amount: '',
      task_question_num: '',
      task_map: []
    };
  },
  mounted () {
    let self = this;
    console.log(self);
    self.task_id = this.$route.params.taskid;
    var apiClient  = new ApiClient('http://localhost:8000');
    apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization')
    self.client = apiClient
    var usersApi = new UsersApi(apiClient);
    self.user = usersApi
    var tasksApi = new TasksApi(apiClient);
    self.task = tasksApi
    var my_username = "";
    self.user.getMeUsersMeGet((error, data, response) => {
      let res = JSON.parse(response['text']);
      my_username = res.username;
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/senderlogin');
        return;
      }
      // 判断是否已领取该任务 // 笨方法遍历
      var list_tasks_claimed = eval(res.tasks_claimed);
      for (var i = 0; i < list_tasks_claimed.length; i++) {
        if (list_tasks_claimed[i] == self.task_id) {
          self.claim = true;
          self.answer = false;
          document.getElementById("claim_button").innerHTML = "已接受任务";
          document.getElementById("start_button").innerHTML = "继续答题 > ";
        }
      }
    })
    self.task.getTaskTasksTaskIdGet(self.task_id, (error, data, response) => {
      let res = JSON.parse(response['text'])

      console.log(res)

      self.task_amount = res.responses_required;
      self.task_brief = res.introduction;
      self.task_name = res.name;
      self.task_tags = eval(res.tags);
      console.log(self.task_tags);
      self.task_credit = res.credits;
      self.task_question_num = res.questions.length;
      // 识别任务类型
      for (var i = 0; i < self.task_tags.length; i++) {
        var cur_tag = self.task_tags[i];
        if (cur_tag == "文字分类" || cur_tag == "图片分类" || cur_tag == "音频分类" || cur_tag == "图片打标") {
          self.task_type = cur_tag;
        }
      }
      // 未知任务类型
      if (self.task_type == '')
        self.task_type = "未知类型";
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
      // 生成question顺序序号与question_id的map
      for (var i = 0; i < self.task_question_num; i++) {
        self.task_map[i] = res.questions[i].question_id;
      }
    })
    self.task.getCoverTasksTaskIdCoverImageGet(self.task_id, (error, data, response) => {
      if (response.status == 400){
        self.task_cover = '../default_cover.jpeg'
      } else{
        let binaryData = [];
        binaryData.push(response.body);
        let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
        // let imageObjectURL = window.URL.createObjectURL(response.body);
        self.task_cover = imageObjectURL
      }
    })
    
    
    
  },
  methods: {
    claim_task() {
      this.task.claimTaskTasksTaskIdClaimPost(this.task_id, (error, data, response) => {
        let res = JSON.parse(response['text'])
        // console.log(res)
      })
      this.claim = true;
      this.answer = false;
      this.$message({
          message: '你已成功接收该任务，开始答题吧！',
          type: 'success'
        });
      document.getElementById("claim_button").innerHTML = "已接受任务";
    },
    start_task() {
      if (this.task_type == "文字分类") {
        this.$router.push({
        name:'question_text',
        params:{
          task_map: this.task_map,
          taskid: this.task_id,
          task_type: this.task_type,
          which_question: 0
        }
      })
      } else if (this.task_type == "图片分类") {
        this.$router.push({
        name:'question_image_classify',
        params:{
          task_map: this.task_map,
          taskid: this.task_id,
          task_type: this.task_type,
          which_question: 0
        }
      })
      }  else if (this.task_type == "图片打标") {
        this.$router.push({
        name:'question_image_identify',
        params:{
          task_map: this.task_map,
          taskid: this.task_id,
          task_type: this.task_type,
          which_question: 0
        }
      })
      }  else if (this.task_type == "音频分类") {
        this.$router.push({
        name:'question_audio',
        params:{
          task_map: this.task_map,
          taskid: this.task_id,
          task_type: this.task_type,
          which_question: 0
        } 
      })
      }  else {
        console.log("TASK TYPE ERROR");
      }
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
  padding: 0px;
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
::v-deep .el-button--primary.is-disabled {
  border-color: #d7d0f0ef;
  background-color: #d7d0f0ef;
  border-radius: 8px;
  border-width: 0;
  margin-right: 10px;
}
::v-deep .el-button--primary.is-disabled:hover {
  border-color: #d7d0f0ef;
  background-color: #d7d0f0ef;
  border-radius: 8px;
  border-width: 0;
  margin-right: 10px;
}
.button_placeholder {
  width: 30px;
}

#claim_button {
  margin-right: 10px;
}
</style>