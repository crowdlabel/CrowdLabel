<template>
  <div class="all">
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">任务大厅</h3>
        <a class="my_account" data-external="true" href="/myaccount">
            <img :src="profile_pic" class="profile" alt="label"/>
        </a>
      </div>
        
    </div>
    <div class="body">
        <div class="left_nav">
            <ul class="left_nav_list_top">
                <li>
                    <a aria-current="page" class="left_nav_list_item left_nav_list_item_active" data-external="true" href="/projects">
                        <img src="../assets/folder_active.png" height="21" width="20">
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
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/draftbox">
                        <img src="../assets/draftbox.png" height="21" width="21">
                        <p class="list_item_title">草稿箱</p>
                    </a>
                </li>
                <li tag="li" class="left_nav_spacer">
                </li>
            </ul>
            <ul class="left_nav_list_bottom">
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/myaccount">
                        <img src="../assets/settings.png" height="20" width="20">
                        <p class="list_item_title">设置</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="https://github.com/crowdlabel">
                        <img src="../assets/about.png" height="20" width="20">
                        <p class="list_item_title">关于我们</p>
                    </a>
                </li>
            </ul>
        </div>
        <div class="main_body">
            <div class="search_bar">
                <el-input v-model="input" placeholder="搜索任务"></el-input>
                <el-button type="primary" icon="el-icon-search" @click="searchWithID()"></el-button>
            </div>
            <div class="filter">
              <p class="title_filter">筛选：</p>
              <div>
              <el-radio-group v-model="taskType" size="small" @change="chooseType()">
                <el-radio-button label="all">全部</el-radio-button>
                <el-radio-button label="text" >文字分类</el-radio-button>
                <el-radio-button label="img_classify" >图片分类</el-radio-button>
                <el-radio-button label="img_borderbox" >图片打标</el-radio-button>
                <el-radio-button label="audio">音频分类</el-radio-button>
              </el-radio-group>
              </div>
            </div>
            <div class="order_by">
              <p class="title_order_by">排序：</p>
              <el-radio-group v-model="sortOrder" size="small" @change="chooseOrder()">
                <el-radio-button label="date">发布时间</el-radio-button>
                <el-radio-button label="credits">积分数量</el-radio-button>
              </el-radio-group>
            </div>
            <div class="display_projects">
              <div class="display_items" v-for="(item, index) in tasks_total.slice((currentPage-1)*pageSize, currentPage*pageSize)">
                <el-card :body-style="{ padding: '0px' }" @click.native="seeDetails(item.task_id)">
                    <img :src=item.cover alt="" class="project_image" >
                    <div style="padding: 0px;">
                      <p class="project_title">{{item.name}}</p>
                      <div class="bottom clearfix">
                      </div>
                    </div>
                  </el-card>
              </div>
            </div>
            <div class="pagination">
              <el-pagination
                background
                :page-size="6"
                :current-page="currentPage.sync"
                @current-change="handleCurrentChange"
                layout="total, prev, pager, next"
                :total=tasks_total.length>
              </el-pagination>
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
import { TasksApi } from '@/crowdlabel-api/src';

export default {
  data() {
    return {
      pageSize: 6,
      currentPage: 1,
      client: '',
      task: '',
      user: '',
      userid: '',
      usercredits: '',
      imageObject: '',
      tasks_total: [],
      page_num: 100,
      input: '',
      taskType: 'all',
      sortOrder: 'date',
      profile_pic: ''
    };
  },
  methods: {
    handleCurrentChange(val) {
      this.currentPage=val;
    },
    seeDetails(task_id) {
      this.$store.commit('changeTaskID', task_id);
      this.$router.push({
        name:'project_detail',
      })
    },
    chooseType() {
      let self = this
      self.tasks_total = []
      var taglist = []
      if(self.taskType=='text'){
        taglist.push("文字分类")
      }else if(self.taskType=='img_classify'){
        taglist.push("图片分类")
      }else if(self.taskType=='img_borderbox'){
        taglist.push("图片打标")
      }else if(self.taskType=='audio'){
        taglist.push("音频分类")
      }
      self.task.searchTasksTasksPut({
        "name": self.input,
        "tags" : taglist,
        "sort_criteria": self.sortOrder,
        "sort_ascending": false,
      }, (error, data, response) => {
        if (error == 'Error: Unauthorized') {
          localStorage.removeItem('Authorization');
          this.$router.push('/receiverlogin');
        }
        let res = JSON.parse(response['text'])
        console.log(res)
        let taskslist = res['tasks']
        var counter = 0
        taskslist.forEach(function(element) {
          var c = { task_id:element['task_id'], name:element['name'], cover:''}
          self.tasks_total.push(c)
          var index = counter;
          counter++;
          self.task.getCoverTasksTaskIdCoverImageGet(element['task_id'], (error, data, response) => {
            if (response.status == 400){
              self.tasks_total[index].cover = '../default_cover.jpeg'
            } else {
              let binaryData = [];
              binaryData.push(response.body);
              let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
              // let imageObjectURL = window.URL.createObjectURL(response.body);
              self.imageObject = imageObjectURL
              self.tasks_total[index].cover = self.imageObject
            }
          })
        })
      })
    },
    chooseOrder(){
      let self = this
      self.tasks_total = []
      var taglist = []
      if(self.taskType=='text'){
        taglist.push("文字分类")
      }else if(self.taskType=='img_classify'){
        taglist.push("图片分类")
      }else if(self.taskType=='img_borderbox'){
        taglist.push("图片打标")
      }else if(self.taskType=='audio'){
        taglist.push("音频分类")
      }
      self.task.searchTasksTasksPut({
        "name": self.input,
        "tags" : taglist,
        "sort_criteria": self.sortOrder,
        "sort_ascending": false,
      }, (error, data, response) => {
        if (error == 'Error: Unauthorized') {
          localStorage.removeItem('Authorization');
          this.$router.push('/receiverlogin');
        }
        let res = JSON.parse(response['text'])
        console.log(res)
        let taskslist = res['tasks']
        var counter = 0
        taskslist.forEach(function(element) {
          var c = { task_id:element['task_id'], name:element['name'], cover:''}
          self.tasks_total.push(c)
          var index = counter;
          counter++;
          self.task.getCoverTasksTaskIdCoverImageGet(element['task_id'], (error, data, response) => {
            if (response.status == 400){
              self.tasks_total[index].cover = '../default_cover.jpeg'
            } else {
              let binaryData = [];
              binaryData.push(response.body);
              let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
              // let imageObjectURL = window.URL.createObjectURL(response.body);
              self.imageObject = imageObjectURL
              self.tasks_total[index].cover = self.imageObject
            }
          })
        })
      })
    },
    searchWithID(){
      let self = this
      self.tasks_total = []
      var taglist = []
      if(self.taskType=='text'){
        taglist.push("文字分类")
      }else if(self.taskType=='img_classify'){
        taglist.push("图片分类")
      }else if(self.taskType=='img_borderbox'){
        taglist.push("图片打标")
      }else if(self.taskType=='audio'){
        taglist.push("音频分类")
      }
      self.task.searchTasksTasksPut({
        "name": self.input,
        "tags" : taglist,
        "sort_criteria": self.sortOrder,
        "sort_ascending": false,
      }, (error, data, response) => {
        if (error == 'Error: Unauthorized') {
          localStorage.removeItem('Authorization');
          this.$router.push('/receiverlogin');
        }
        let res = JSON.parse(response['text'])
        console.log(res)
        let taskslist = res['tasks']
        var counter = 0
        taskslist.forEach(function(element) {
          var c = { task_id:element['task_id'], name:element['name'], cover:''}
          self.tasks_total.push(c)
          var index = counter;
          counter++;
          self.task.getCoverTasksTaskIdCoverImageGet(element['task_id'], (error, data, response) => {
            if (response.status == 400){
              self.tasks_total[index].cover = '../default_cover.jpeg'
            } else {
              let binaryData = [];
              binaryData.push(response.body);
              let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
              // let imageObjectURL = window.URL.createObjectURL(response.body);
              self.imageObject = imageObjectURL
              self.tasks_total[index].cover = self.imageObject
            }
          })
        })
      })
    },
  },
  directives: {
    focus: {
      inserted: function(el) {
        el.focus();
      }
    }
  },
  created () {

  },
  mounted () {
    let self = this
    let base = this.$root.basePath
    var apiClient  = new ApiClient(base);
    apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization')
    self.client = apiClient
    var usersApi = new UsersApi(apiClient);
    self.user = usersApi
    var tasksApi = new TasksApi(apiClient);
    self.task = tasksApi
    self.user.getMeUsersMeGet((error, data, response) => {
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/receiverlogin');
        return;
      }
      let a = JSON.parse(response['text'])
      if (a.user_type != 'respondent'){
        localStorage.removeItem('Authorization');
        this.$router.push('/');
        return;
      }
      self.userid = a['username']
      self.usercredits = a['credits']
    })
    self.user.getPfpUsersMeProfilePictureGet((error, data, response) => {
      if (response.status == 404){
        self.profile_pic = '../my_account.svg'
      } else {
        let binaryData = [];
        binaryData.push(response.body);
        let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
        self.profile_pic = imageObjectURL
      }
    })
    self.tasks_total = []
    self.task.searchTasksTasksPut({
      "sort_criteria": "date",
      "sort_ascending": false
    }, (error, data, response) => {
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/receiverlogin');
      }
      let res = JSON.parse(response['text'])
      let taskslist = res['tasks']
      var counter = 0
      console.log(taskslist)
      taskslist.forEach(function(element) {
        var c = { task_id:element['task_id'], name:element['name'], cover:''}
        self.tasks_total.push(c)
        var index = counter;
        counter++;
        self.task.getCoverTasksTaskIdCoverImageGet(element['task_id'], (error, data, response) => {
          if (response.status == 400){
            self.tasks_total[index].cover = '../default_cover.jpeg'
          } else {
            let binaryData = [];
            binaryData.push(response.body);
            let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
            // let imageObjectURL = window.URL.createObjectURL(response.body);
            self.imageObject = imageObjectURL
            self.tasks_total[index].cover = self.imageObject
          }
        })
      })
    })
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

a {
  text-decoration:none;
}
.all {
  min-width: 1150px;
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
.my_account {
    align-items: center;
    align-self: center;
    cursor: pointer;
    display: flex;
    justify-content: center;
    position: relative;
    margin-right: 17px;
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
}

.search_bar {
  flex-direction: row;
  display: flex;
}

::v-deep .el-input {
  width: 75% !important;
  margin-left: 100px;
}

::v-deep .el-input__inner { 
  font-size: 15px;
  min-width: 400px;
  height: 50px;
  border-radius: 0px;
  margin-top: 40px;
  margin-right: 0px;
}

::v-deep .el-input__inner:focus { 
  border-radius: 0px;
  border-color: #5D3BE6;
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
  margin: 20px 100px 0px 100px;
}
.title_filter {
  padding: 0px 8px 0px 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}

::v-deep .el-radio-group {
  border-color: #5D3BE6;
}
::v-deep .el-radio-button__inner {
  background: #fff;
  border-color: #5D3BE6;
  color:#5D3BE6;
  font-size: 12.5px;
  min-width: 80px;
  align-items:center;
  box-shadow:none;
  outline: none;
}
::v-deep .el-radio-button__orig-radio:hover + .el-radio-button__inner {
  background: #5D3BE6;
  border-color: #5D3BE6;
  color: #fff;
}
::v-deep .el-radio-button__orig-radio:checked + .el-radio-button__inner{
  background: #5D3BE6;
  border-color: #5D3BE6;
  box-shadow:none;
  color: #fff;
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
  margin: 0px 100px 0px 100px;
}
.title_order_by {
  padding: 0px 8px 0px 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}

.display_projects {
  flex-direction: row;
  display: flex;
  align-items:left;
  margin: 20px 100px;
  flex-wrap: wrap;
  width: 80%;
  height: 360px !important;
}

.display_items{
  width: 33.3333%;
  float: left;
  height:180px;
  display: flex;
  flex-direction: center;
  align-items: center;
  box-sizing: border-box;
  cursor: pointer;
}


.project {
  margin: 0px 30px;
}

::v-deep .el-pagination {
  margin-top: 20px;
  margin-bottom: 20px;
}
::v-deep .el-pagination.is-background .el-pager li.active {
  background-color: #5D3BE6 !important;
}
::v-deep .el-pagination.is-background .el-pager li.active:hover {
  color: #fff !important;
}
::v-deep .el-pagination.is-background .el-pager li:hover {
  background-color: #5D3BE6 !important;
  color: #fff !important;
}

.project_title {
  text-align: left;
  margin: 0px 9px 8px 9px;
  font-size: 13px;
}
.project_image {
  height: 130px;
  width: 250px;
}

.profile {
  height: 28px;
  width: 28px;
  border-radius: 50%;
}
</style>