<template>
  <div class="all">
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">草稿箱</h3>
          <a class="notifications" data-external="true" href="/notifications">
            <img src="../assets/notifications.svg" alt="label" height="24"/>
          </a>
      </div>
        <a class="my_account" data-external="true" href="/myaccount">
            <img src="../assets/my_account.svg" alt="label" height="24"/>
        </a>
    </div>
    <div class="body">
        <div class="left_nav">
            <ul class="left_nav_list_top">
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/projects">
                        <img src="../assets/folder.png" height="21" width="20">
                        <p class="list_item_title">任务大厅</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/history">
                        <img src="../assets/history.png" height="19" width="20">
                        <p class="list_item_title">历史记录</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/credits">
                        <img src="../assets/credits.png" height="19" width="20">
                        <p class="list_item_title">我的积分</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item left_nav_list_item_active" data-external="true" href="/draftbox">
                        <img src="../assets/draftbox_active.png" height="21" width="21">
                        <p class="list_item_title">草稿箱</p>
                    </a>
                </li>
                <li tag="li" class="left_nav_spacer">
                </li>
            </ul>
            <ul class="left_nav_list_bottom">
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/settings">
                        <img src="../assets/settings.png" height="20" width="20">
                        <p class="list_item_title">设置</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/about_us">
                        <img src="../assets/about.png" height="20" width="20">
                        <p class="list_item_title">关于我们</p>
                    </a>
                </li>
            </ul>
        </div>
        <div class="main_body">
            <div class="scroll_view">
              <el-scrollbar style="height: 100%">
                <!-- 用于展示下拉，填充的内容 -->
                <div class="scroll_element" v-for="(item, index) in projectsList" :key="index" @click="seeDetails(item.task_id)">
                  <img :src=item.cover class="project_image">
                  <div class="scroll_element_text">
                    <h4 class="project_title">{{ item.name }}</h4>
                    <p class="project_detail">任务类型: {{ item.type }}</p>
                    <p class="project_detail">任务标签: {{ item.tags }}</p>
                    <p class="project_detail">答题进度: {{ item.progress }}</p>
                  </div>
                </div>
              </el-scrollbar>
            </div>
        </div>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { ApiClient } from '@/crowdlabel-api/src';
import { UsersApi } from '@/crowdlabel-api/src';
import { AuthApi } from '@/crowdlabel-api/src';
import { TasksApi } from '@/crowdlabel-api/src';
export default {
  data() {
    return {
      client:'',
      user:'',
      task:'',
      auth:'',
      projectsList: []
    };
  },
  mounted() {
    let self = this;
    let base = this.$root.basePath
    var apiClient  = new ApiClient(base);
    apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization')
    self.client = apiClient
    var usersApi = new UsersApi(apiClient);
    self.user = usersApi
    var authApi = new AuthApi(apiClient);
    this.auth = authApi
    var tasksApi = new TasksApi(apiClient);
    self.task = tasksApi;
    self.user.getMeUsersMeGet((error, data, response) => {
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/receiverlogin');
      }
      let res = JSON.parse(response["text"]);
      let tasks_claimed = res["tasks_claimed"];
      console.log(tasks_claimed)
      for (let i = 0; i < tasks_claimed.length; i++) {
        let _task_id = tasks_claimed[i];
        // console.log(tasks_claimed[i])
        // console.log(_task_id)
        self.task.getTaskTasksTaskIdGet(_task_id, (error, data, response) => {
          let res = response.body;
          let _name = res.name;
          let _tags = '';
          let _type = '';
          let _total_question_num = res.questions.length;
          let task_tags = res.tags;
          for (var k = 0; k < task_tags.length; k++) {
            _tags += task_tags[k];
            if (k != task_tags.length - 1) {
              _tags += ", ";
            }
            if (task_tags[k] == "文字分类" || task_tags[k] == "图片分类" || task_tags[k] == "图片打标" || task_tags[k] == "音频分类")
              _type = task_tags[k];
          }
          var cur_task = {task_id: _task_id, name: _name, type: _type, tags: _tags, progress: _total_question_num, cover: ''};
          self.projectsList.push(cur_task);
          let index_p = i;
          self.task.getProgressTasksTaskIdProgressGet(res.task_id, (error, data, response) => {
            let res2 = JSON.parse(response['text']);
            // console.log(res.task_id);
            console.log(res2)
            let total_questions = self.projectsList[i].progress;
            let _progress = "" + parseInt(res.progress + 1) + " / " + total_questions;
            console.log(parseInt(res.progress + 1))
            self.projectsList[i].progress = _progress;
            self.task.getCoverTasksTaskIdCoverImageGet(_task_id, (error, data, response) => {
              let _cover = '';
              if (response.status == 400){
                _cover = '../default_cover.jpeg'
              } else {
                let binaryData = [];
                binaryData.push(response.body);
                let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
                _cover = imageObjectURL;
              }
              self.projectsList[i].cover = _cover;
            });
          });
        });
      }
    })
  },
  methods: {
    seeDetails(task_id) {
      console.log("CLICKED")
      this.$store.commit('changeTaskID', task_id);
      this.$router.push({
        name:'project_detail',
      })
    }
  } 
}
</script>

<style scoped>
@import '@/assets/font/font.css';

.all {
  min-width: 1000px;
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
    min-width: 230px;
    max-width: 230px;
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
.notifications {
    align-items: center;
    align-self: center;
    cursor: pointer;
    display: flex;
    justify-content: center;
    position: relative;
}
.my_account {
    align-items: center;
    align-self: center;
    cursor: pointer;
    display: flex;
    justify-content: center;
    margin-left: 10px;
    margin-right: 20px;
    position: relative;
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
    max-width: 230px;
    min-width: 230px;
    box-shadow: 1.2px 0 0 0 rgb(0 0 0 / 10%);
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
}
.left_nav_list_top {
    box-sizing: border-box;
    list-style-type: none;
    flex: 1;
    flex-direction: column;
    margin: 0;
    padding: 12px;
    height: calc(100vh - 50px - 132.2px);
    min-height: 230px;
}
.left_nav_list_bottom {
    box-sizing: border-box;
    list-style-type: none;
    border-top: 1.2px solid rgba(0,0,0,.1);
    flex: 1;
    flex-direction: column;
    position: relative;
    bottom: 0;
    margin: 0;
    padding: 12px;
}
.left_nav_spacer {
    height: calc(100vh - 329.2px);
    flex: 1;
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
    padding: 15px;
    font-size: 15px;
}

.main_body {
    box-sizing: border-box;
    flex-direction: column;
    position: relative;
    display: flex;
    flex:1;
    height: calc(100vh - 50px);
    min-height: 140px;
}
::v-deep .el-button--primary {
  margin-top: 40px;
  margin-right: 80px;
  padding: 0px 20px;
  border-width: 0px;
  border-radius: 0px 4px 4px 0px;
  background-color: #5D3BE6;
  font-size: 20px;
  min-width: 80px;
}

::v-deep .el-button--primary:hover{
  background-color: rgba(84,47,238,.8);
}

::v-deep .el-button--primary:focus {
  background-color: #5D3BE6;
}

.filter {
  flex-direction: row;
  display: flex;
  align-items:center;
  margin: 20px 60px 0px 60px;
}
.title_filter {
  padding: 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}
::v-deep .el-button--success {
  margin: 0px 0px 0px 10px;
  height: 30px;
  padding: 0px 0px !important;
  border-width: 0.5px;
  background-color: #5D3BE6;
  font-size: 12.5px;
  min-width: 80px;
}
::v-deep .el-button--success:hover{
  background-color: #5D3BE6;
}

::v-deep .el-button--success:focus {
  background-color: #5D3BE6;
}

::v-deep .el-button--default.is-round {
  margin: 0px 0px 0px 10px;
  height: 30px;
  border-width: 0.5px;
  padding: 0px 0px !important;
  border-color: #5D3BE6;
  color:#5D3BE6;
  font-size: 12.5px;
  min-width: 80px;
}
::v-deep .el-button--default.is-round:hover{
  background-color: #5D3BE6;
  border-width: 0.5px;
  color: #fff;
}

::v-deep .el-button--default.is-round:focus {
  background-color: #5D3BE6;
  border-width: 0.5px;
  color: #fff;
}

.order_by {
  flex-direction: row;
  display: flex;
  align-items:center;
  margin: 0px 60px 0px 60px;
}
.title_order_by {
  padding: 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}

.scroll_view {
  height: calc(100vh - 50px);
  min-height: 362px;
}

.scroll_element {
  height: fit-content;
  border-bottom: 1.2px solid rgba(0,0,0,.1);
  flex-direction: row;
  cursor: pointer;
  display: flex;
  padding: 20px 25px;
}

.scroll_element_text {
  margin: 0px 20px;
  flex-direction: column;
  display: flex;
  align-items: flex-start;
}
.project_title {
  margin: 0px 0px 3px 0px;
}
.project_detail {
  margin: 0px;
  font-size: 10px;
  color: rgba(0,0,0,.7);
}
.project_image {
  height: 87px;
  width: 100px;
  border-radius: 10%;
  align-self:center;
}
</style>