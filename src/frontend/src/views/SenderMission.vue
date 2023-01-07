<template>
    
  <div class="all">
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">任务大厅</h3>
        <a class="my_account" data-external="true" href="/senderaccount">
          <img :src="profile_pic" class="profile" alt="label"/>
        </a>
      </div>
      
    </div>
    <div class="body">
        <div class="left_nav">
            <ul class="left_nav_list_top">
                <li>
                    <a aria-current="page" class="left_nav_list_item left_nav_list_item_active" data-external="true" href="/sendermission">
                        <img src="../assets/folder_active.png" height="21" width="20">
                        <p class="list_item_title">我的任务</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/sendercredits">
                        <img src="../assets/credits.png" height="19" width="20">
                        <p class="list_item_title">我的积分</p>
                    </a>
                </li>
                <li tag="li" class="left_nav_spacer">
                </li>
            </ul>
            <ul class="left_nav_list_bottom">
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/senderaccount">
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

        <el-dialog
          :visible.sync="dialogVisible"
          width="40%"
          min-width="400px"
          class="dialogClass"
          border-radius="12px">
          <div class="type_page">
            <div class="create_h2">
              <h2 id="create_title">创建您新任务</h2>
            </div>
            <div class="create_main">
              <el-form label-width="80px" ref="form" :model="form" :rules="rules">
                <!-- <el-form-item prop="name" class="name_item">
                  <el-input placeholder="请输入任务名称"  class="mission_name" v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="任务简介:" class="mission_brief" prop="brief">
                  <el-input type="textarea" v-model="form.brief" class="brief_input"></el-input>
                </el-form-item>
                <el-form-item label="任务详情:" class="mission_details" prop="details">
                  <el-input type="textarea" v-model="form.details" class="details_input"></el-input>
                </el-form-item>
                <el-form-item label="上传封面:" class="mission_file">
                  <el-upload class="upload_file" action="none"
                    :headers="{ 'Content-Type': 'multipart/form-data'}"
                    accept=".jpg, .png"
                    :auto-upload="false"
                    :on-change="handleChange"
                    :limit="1"
                    :file-list="form.cover"
                    >
                    <el-button type="primary" size="small" class="click_upload_btn">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传JPG和PNG文件</div>
                  </el-upload>
                </el-form-item> -->
                <el-form-item label="上传文件:" class="mission_file" required>
                  <el-upload class="upload_file" action="none"
                    :headers="{ 'Content-Type': 'multipart/form-data'}"
                    accept=".zip, .rar"
                    :auto-upload="false"
                    :on-change="handleZip"
                    :limit="1"
                    :file-list="form.zipfile"
                    >
                    <el-button type="primary" size="small" class="click_upload_btn">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传zip或rar文件</div>
                  </el-upload>
                </el-form-item>
                <!-- <el-form-item prop="amount" label="任务份额:" class="mission_credits">
                  <el-input placeholder="请输入任务总份数"  class="credits_input" v-model="form.amount"></el-input>
                </el-form-item>
                <el-form-item prop="credits_each" label="积分奖励:" class="mission_credits">
                  <el-input placeholder="请输入每份任务报酬积分"  class="credits_input" v-model="form.credits_each"></el-input>
                </el-form-item> -->
                <el-form-item>
                  <el-button type="primary" class="create_now" @click="create_new_project">立即创建</el-button>
                  <el-button type="default" class="cancel" @click="backToMission">取消</el-button>
                </el-form-item>
              </el-form>
            </div>
          </div>
        </el-dialog>

        <el-dialog
          :visible.sync="UploadMissionInfo"
          width="50%"
          min-width="800px"
          class="UploadInfoClass"
          border-radius="12px">
          <h2>任务文件上传说明</h2>
          <div class="dabao_body">
            <div class="dabao_title">
              <h3 class="dabao_subtitle">一、打包格式</h3>
              <div class="dabao_content">
                <p class="dabao_words"> - 最终上传文件要求格式为 zip 或者 rar ，大小不超过10GB</p>
              </div>
            </div>
            <div class="dabao_title">
              <h3 class="dabao_subtitle">二、文件夹内部格式</h3>
              <div class="dabao_content">
                <p class="dabao_words"> - zip文件夹中包括一个 task.json 文件和若干题目资源文件</p>
                <p class="dabao_words"> - 文字分类的每道题的题干存放在每道题单独对应的 txt 文件中</p>
                <p class="dabao_words"> - 其他的图片资源格式要求为 jpg 或者 png</p>
              </div>
            </div>
            <div class="dabao_title">
              <h3 class="dabao_subtitle">三、task.json文件格式</h3>
              <div class="dabao_content">
                <p class="dabao_words"> - task.json 文件中包含整个任务的各种设置，是最重要的文件</p>
                <p class="dabao_words"> - task.json 文件中是一个大的字典</p>
                <p class="dabao_words"> - 字典中包括"name", "credits", "introduction", "description", "tags", "responses_required", "cover_image", "questions" 这8个不同的key</p>
                <p class="dabao_words"> - "name"表示任务的名称，是一个字符串</p>
                <p class="dabao_words"> - "credits"表示提供给每一个答题者的积分数量，是一个int值</p>
                <p class="dabao_words"> - "introduction"表示任务的简介，是一个字符串</p>
                <p class="dabao_words"> - "description"表示任务的详情，是一个字符串</p>
                <p class="dabao_words"> - "tags"表示任务的标签，是一个字符串，但必须包含“图片分类”、“文字分类”、“图片打标”、“音频分类”这四种中的一种（且只有一种）</p>
                <p class="dabao_words"> - "responses_required"表示任务的份数，是一个int值</p>
                <p class="dabao_words"> - "cover_image"表示任务的封面，是一个字符串，里面是对应图片资源的完整文件名（和task.json处于同一目录下），比如"cover.jpg"</p>
                <p class="dabao_words"> - "questions"表示任务中问题的具体信息，是一个数组，每个数组元素信息要求如下：</p>
                <p class="dabao_subwords"> 1、每个question数组元素都是一个字典，对应一道题，其中包括5个不同的key</p>
                <p class="dabao_subwords"> 2、每道题有唯一的"question_id"，用户可以随意设置，是一个int值</p>
                <p class="dabao_subwords"> 3、每道题有一个"question_type"，从"open"、"single_choice"、"bounding_box"、"multi_choice"选一个</p>
                <p class="dabao_subwords"> 4、每道题有一个"prompt"，是问题是描述，是一个字符串</p>
                <p class="dabao_subwords"> 5、每道题可以有一个"resource"，是一个字符串，存放的是对应资源的完整名称，比如"1.jpg"</p>
                <p class="dabao_subwords"> 6、如果这道题是一个单选或者多选题，则会有一个"options"，里面是一个字符串数组，存放各种选项，选项数为2-7个</p>
              </div>
            </div>
            <div class="dabao_title">
              <h3 class="dabao_subtitle">四、文件样例</h3>
              <div class="dabao_content">

<pre>{
    "name": "Image",
    "credits": 2,
    "introduction": "",
    "description": "Image",
    "tags": ["图片分类"],
    "responses_required": 2,
    "cover_image": "2.jpg",
    "questions": [
        {
            "question_id": 1,
            "question_type": "single_choice",
            "prompt": "What is in the image?",
            "resource": "1.jpg",
            "options": ["bike", "dog", "person"]
        },
        {
            "question_id": 5,
            "question_type": "single_choice",
            "prompt": "What is in the image?",
            "resource": "3.jpg",
            "options": ["bike", "rock", "car", "school"]
        },
        {
            "question_id": 3,
            "question_type": "single_choice",
            "prompt": "What is in the image?",
            "resource": "2.jpg",
            "options": ["bike", "dog", "car"]
        }
    ]
}</pre>
<br>

            <div class="dabao_title">
                <h3 class="dabao_subtitle">五、目录结构</h3>
                <div class="dabao_content">
<pre>.
└── your-folder-name/
    ├── 1.jpg
    ├── 2.jpg
    ├── 3.jpg
    └── task.json</pre></div>
            </div>


              </div>
            </div>
            <div class="dabao_title">
              <h3 class="dabao_subtitle">六、注意事项</h3>
              <div class="dabao_content">
                <p class="dabao_words"> - 一定要按照格式准备文件，然后进行上传，否则会上传失败</p>
                <p class="dabao_words"> - 相同的资源文件可以即作为题目，也可以作为封面。</p>
                <p class="dabao_words"> - 假如没有选择封面图片，则会使用系统默认的封面图片，不会影响上传</p>
                <p class="dabao_words"> - 祝好！</p>
              </div>
            </div>
          </div>
        </el-dialog>

        <div class="main_body">
            <div class="search_bar">
                <el-input placeholder="搜索任务" id="specific_name" v-model="search_input"></el-input>
                <el-button type="primary" icon="el-icon-search" @click="searchSpecific"></el-button>
            </div>
            <div class="filter">
              <p class="title_filter">筛选：</p>
              <el-radio-group v-model="taskType" size="small" @change="chooseType()">
                <el-radio-button label="all">全部</el-radio-button>
                <el-radio-button label="text" >文字分类</el-radio-button>
                <el-radio-button label="img_classify" >图片分类</el-radio-button>
                <el-radio-button label="img_borderbox" >图片打标</el-radio-button>
                <el-radio-button label="audio">音频分类</el-radio-button>
              </el-radio-group>
              <el-button type="default" round @click="uploadInfo" id="format_download">任务上传说明</el-button>
              <el-button type="primary" round @click="createProject" id="create">创建任务</el-button>
            </div>
            
            <div class="display_projects">
              <div class="display_items" v-for="(item, index) in tasks_info.slice((currentPage-1)*pageSize, currentPage*pageSize)">
                <el-card :body-style="{ padding: '0px' }" @click.native="seeDetails(item.task_id)">
                    <img :src=item.cover alt='' class="project_image" >
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
                :total=taskslist.length>
              </el-pagination>
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
    // page_num = 5;
    var validateName = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务名称'))
      } else {
        callback();
      }
    };
    var validateBrief = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务简介'))
      } else {
        callback();
      }
    };
    var validateDetails = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务详情'))
      } else {
        callback();
      }
    };
    var validateCreditsEach = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入每份任务积分奖励'))
      } else {
        callback();
      }
    };
    var validateAmount = (rule, value, callback) => {
      if (value === ''){
          callback(new Error('请输入任务总份数'))
      } else {
        callback();
      }
    };
    return {
      profile_pic:'',
      pageSize: 6,
      currentPage: 1,
      search_input:'',
      UploadMissionInfo: false,
      dialogVisible: false,
      client: '',
      task: '',
      user: '',
      userid: '',
      usercredits: '',
      tasks_info: [],
      taskslist: '',
      task_name: [],
      taskType: 'all',
      task_cover_image: [],
      tasksinfo: {
        responses_required: '',
        responses_completed: ''
      },
      imageObject: '',
      // 
      multipartFile: [],
      form: {
        // name: '',
        // brief: '',
        // details: '',
        // credits_each: '',
        // amount: '',
        // cover: [],
        file: '',
        zipfile: []
      },
      rules: {
        name: [
          { validator: validateName, trigger: 'blur'}
        ],
        brief: [
          { validator: validateBrief, trigger: 'blur'}
        ],
        details: [
          { validator: validateDetails, trigger: 'blur'}
        ],
        credits_each: [
          { validator: validateCreditsEach, trigger: 'blur'}
        ],
        amount: [
          { validator: validateAmount, trigger: 'blur'}
        ],
      },
    }
  },
  methods: {
    searchSpecific () {
      let self = this
      self.tasks_info = []
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
      let requesterlist = []
      requesterlist.push(self.userid)
      self.task.searchTasksTasksPut({
        "name": self.search_input,
        "requester": requesterlist, 
        "tags" : taglist,
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
          self.tasks_info.push(c)
          var index = counter;
          counter++;
          self.task.getCoverTasksTaskIdCoverImageGet(element['task_id'], (error, data, response) => {
            if (response.status == 400){
              self.tasks_info[index].cover = '../default_cover.jpeg'
            } else {
              let binaryData = [];
              binaryData.push(response.body);
              let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
              // let imageObjectURL = window.URL.createObjectURL(response.body);
              self.imageObject = imageObjectURL
              self.tasks_info[index].cover = self.imageObject
            }
          })
        })
      })
    },
    chooseType() {
      let self = this
      self.tasks_info = []
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
      let requesterlist = []
      requesterlist.push(self.userid)
      self.task.searchTasksTasksPut({
        "name": self.search_input,
        "requester": requesterlist, 
        "tags" : taglist,
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
          self.tasks_info.push(c)
          var index = counter;
          counter++;
          self.task.getCoverTasksTaskIdCoverImageGet(element['task_id'], (error, data, response) => {
            if (response.status == 400){
              self.tasks_info[index].cover = '../default_cover.jpeg'
            } else {
              let binaryData = [];
              binaryData.push(response.body);
              let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
              // let imageObjectURL = window.URL.createObjectURL(response.body);
              self.imageObject = imageObjectURL
              self.tasks_info[index].cover = self.imageObject
            }
          })
        })
      })
    },
    handleCurrentChange(val) {
      this.currentPage=val;
    },
    seeDetails(task_id) {
      this.$store.commit('changeTaskID', task_id);
      this.$router.push({
        name:'sendermissiondetail',
      })
    },
    handleChange(file, fileList) {
      let self = this;
      if (file.size / (1024*1024)>10) {
        self.$message.warning("当前限制文件大小不能大于10MB");
        self.file = '';
        self.form.cover= [];
        return false;
      }
      let suffix = self.getFileType(file.name);
      let suffixArray = ["jpg", "jpeg", "png"];
      if (suffixArray.indexOf(suffix) === -1) {
        self.$message({
          message: "文件格式错误",
          type: "error",
          duration: 2000
        });
        self.file = "";
        self.form.cover=[];
      }else{
        // self.multipartFile.append("cover", file.raw)
        self.file = file.raw;
        self.form.cover = fileList;
      }
    },
    handleZip(file, fileList) {
      let self = this;
      if (file.size / (1024*1024*1024)>10) {
        self.$message.warning("当前限制文件大小不能大于10GB");
        self.file = '';
        self.form.zipfile= [];
        return false;
      }
      let suffix = self.getFileType(file.name);
      let suffixArray = ["zip", "rar"];
      if (suffixArray.indexOf(suffix) === -1) {
        self.$message({
          message: "文件格式错误",
          type: "error",
          duration: 2000
        });
        self.file = "";
        self.form.zipfile=[];
      }else{
        // self.multipartFile.append("file", file.raw)
        self.file = file.raw;
        self.form.zipfile = fileList;
      }
    },
    refresh: function() {
      let self = this
      self.user.getMeUsersMeGet((error, data, response) => {
      if (error == 'Error: Unauthorized') {
        localStorage.removeItem('Authorization');
        this.$router.push('/senderlogin');
      }
      let a = JSON.parse(response['text'])
      self.userid = a['username']
      self.usercredits = a['credits']
      self.taskslist = a['tasks_requested']
      self.tasks_info = []
      var counter = 0
      self.taskslist.forEach(function(element) {
        var c = { task_id:element, name:'', cover:''}
        self.tasks_info.push(c)
        var index = counter;
        counter++;
        self.task.getCoverTasksTaskIdCoverImageGet(element, (error, data, response) => {
          if (response.status == 400){
            self.tasks_info[index].cover = '../default_cover.jpeg'
            // var c = { task_id:element, name:'', cover:'../default_cover.jpeg'}
            self.task.getTaskTasksTaskIdGet(element, (error, data, response) => {
              let b = JSON.parse(response['text'])
              // c.name = b.name
              // self.tasks_info.push(c)
              self.tasks_info[index].name = b.name
            })
          } else {
            let binaryData = [];
            binaryData.push(response.body);
            let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));

            //let imageObjectURL = window.URL.createObjectURL(response.body);
            self.imageObject = imageObjectURL
            self.tasks_info[index].cover = self.imageObject
            // var c = { task_id:element, name:'', cover:self.imageObject}
            self.task.getTaskTasksTaskIdGet(element, (error, data, response) => {
              let b = JSON.parse(response['text'])
              // c.name = b.name
              // self.tasks_info.push(c)
              self.tasks_info[index].name = b.name
            })
          }
        })
      });
      })
    },
    getFileType(name){
      let startIndex = name.lastIndexOf(".");
      if (startIndex !== -1) {
        return name.slice(startIndex+1).toLowerCase();
      } else {
        return ""; 
      }
    },
    backToMission() {
      this.dialogVisible = false;
    },
    uploadInfo () {
      this.UploadMissionInfo = true;
    },
    createProject () {
      this.dialogVisible = true;
    },
    create_new_project () {
      if(this.zipfile === '' || this.zipfile === 'null'){
        alert('You need to upload file');
        return false;
      } else {
        // this.multipartFile.append('username', this.userid);
        // this.multipartFile.append('missionname', this.form.name);
        // this.multipartFile.append('missionamount', this.form.amount);
        // this.multipartFile.append('missioncredits', this.form.credits_each)
        // this.multipartFile.append('missionbrief', this.form.brief);
        // this.multipartFile.append('missiondetails', this.form.details);
        this.task.uploadTaskTasksUploadPost(this.file, (error, data, response) => {
          let a = JSON.parse(response['text'])
          if (response.status == 400 && a.error == 'Insufficient credits'){
            console.log(error, response)
            this.$confirm('积分不足！是否跳转到充值页面?', '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'info',
            }).then(() => {
              this.$router.push('/sendercredits');
            }).catch(() => {
              this.$message({
                type: 'info',
                message: '已取消跳转'
              });
            });
          } else if (response.status==400) {
            this.$confirm(a.error, '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'info',
            }).then(() => {
              
            }).catch(() => {
              
            });
            this.form.zipfile = [];
          } else if(response.status == 200){
            this.form.zipfile = []
            this.file = ''
            this.form.cover = []
            alert('上传成功');
            this.dialogVisible = false
            this.refresh();
          } else if(response.status == 422){
            alert('请上传文件！')
          }
        })
      }
    }
  },
  created() {
    // this.multipartFile = new FormData();
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
        this.$router.push('/senderlogin');
        return;
      }
      let a = JSON.parse(response['text'])
      if (a.user_type != 'requester'){
        localStorage.removeItem('Authorization');
        this.$router.push('/');
        return;
      }
      self.userid = a.username
      self.usercredits = a.credits
      self.taskslist = []
      self.taskslist = a.tasks_requested
      self.tasks_info = []
      var counter = self.taskslist.length - 1
      self.taskslist.forEach(function(element) {
        var c = { task_id:element, name:'', cover:''}
        self.tasks_info.unshift(c)
        var index = counter;
        counter--;
        self.task.getCoverTasksTaskIdCoverImageGet(element, (error, data, response) => {
          if (response.status == 400){
            self.tasks_info[index].cover = '../default_cover.jpeg'
            self.task.getTaskTasksTaskIdGet(element, (error, data, response) => {
              let b = JSON.parse(response['text'])
              self.tasks_info[index].name = b.name
            })
          } else {
            let binaryData = [];
            binaryData.push(response.body);
            let imageObjectURL = window.URL.createObjectURL(new Blob(binaryData));
            self.imageObject = imageObjectURL
            self.tasks_info[index].cover = self.imageObject
            self.task.getTaskTasksTaskIdGet(element, (error, data, response) => {
              let b = JSON.parse(response['text'])
              self.tasks_info[index].name = b.name
            })
          }
        })
      });
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
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

.dialogClass{
  min-width: 400px !important;
}
::v-deep .dialogClass .el-dialog{
  width: 40% !important;
  min-width: 400px;
  border-radius: 12px;
}

::v-deep .UploadInfoClass .el-dialog{
  width: 50% !important;
  min-width: 800px;
  border-radius: 12px;
}
::v-deep .el-dialog__body{
  padding: 0;
}

.all {
  min-width: 1250px;
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
    min-height: 130px;
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
  margin-top:40px;
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
  margin-top: 20px;
  margin-right: 0px;
}

::v-deep .el-input__inner:focus { 
  border-radius: 0px;
  border-color: #5D3BE6;
}

::v-deep .el-button--primary {
  margin-top: 20px;
  margin-right: 80px;
  padding: 0px 20px;
  border-width: 0px;
  border-radius: 0px 4px 4px 0px;
  background-color: #5D3BE6;
  border-color: #5D3BE6;
  font-size: 20px;
  min-width: 80px;
}

::v-deep .el-button--primary:hover{
  background-color: rgba(84,47,238,.8);
  border-color: #5D3BE6;
}

::v-deep .el-button--primary:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
}
::v-deep .el-button.el-button--default:focus, .el-button.el-button--default:hover{
    color: #5D3BE6;
    background-color: #F3EAFF;
}

.filter {
  flex-direction: row;
  display: flex;
  align-items:center;
  margin: 20px 100px 0px 100px;
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
  border-color: #5D3BE6;
  font-size: 12.5px;
  min-width: 80px;
}
::v-deep .el-button--success:hover{
  background-color: #5D3BE6;
}

::v-deep .el-button--success:focus {
  background-color: #5D3BE6;
  border-color: #5D3BE6;
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
  border-color: #5D3BE6;
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
  padding: 0px;
  font-size: 14px;
  color:rgba(0,0,0,.6);
}


.display_projects {
  flex-direction: row;
  display: flex;
  align-items:left;
  margin: 20px 100px;
  margin-bottom:20px;
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
  margin-top: 20px !important;
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

#create{
  position: absolute;
  float: left; 
  top: 115px;
  left: 800px;
  font-size: 16px;
  padding: 12px 24px;
}

#format_download{
  position: absolute;
  float:left;
  top:140px;
  left:700px;
  width:90px;
  padding: 0px 15px;
}

.mission_name{
  float: left;
  margin-left:0px !important;
  margin-top: 0px !important;
  width: 90% !important;
}
::v-deep .el-form-item__content{
  margin-left: 20px !important;
}

::v-deep .el-form-item{
  margin-bottom: 20px;
}

#create_title{
  margin-top:0px;
  margin-bottom:0px !important;
}

.create_now{
  font-size: 16px !important;
  margin-top: 0px !important;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 30px !important;
  border-radius: 10px !important;
}

.cancel{
  font-size: 16px;
  padding-top: 10px !important;
  padding-bottom: 10px !important;
  margin-bottom: 30px !important;
}

.mission_type{
  margin-left: 30px !important;
  margin-right: 30px !important;
}
.mission_file{
  margin-left: 30px !important;
  margin-right: 30px !important;
}

.upload_file{
  float: left;
  width: 100%;
}

::v-deep .el-form-item__label{
  width: 100px !important;
}

.click_upload_btn{
  position: relative !important;
  width: 70px;
  border-radius: 8px !important;
  float:left;
  margin-top: 0px;
  font-size:12px;
  padding: 8px 2px;

}

::v-deep .el-upload__tip{
  float:left;
  position: relative;
  width: 140px;
  line-height: 25px;
}

::v-deep .el-radio-group{
  position: relative;
  float: left;
}
.mission_name{
  font-size: 14px !important;
  /* height: 36px !important; */
  line-height:30px !important;
}

::v-deep .el-form-item__label{
  position: relative;
  float: left !important;;
}

.mission_brief{
  margin-left: 30px;
  margin-right: 30px;
}

.mission_details{
  margin-left: 30px;
  margin-right: 30px;
}

::v-deep .el-textarea{
  width:80% !important;
  min-height: 40px !important;
  left: -20px;
}

::v-deep .el-upload-list{
  float: left;
  width: 40%;
}

::v-deep .el-upload{
  position: relative !important;
  top: 7px;
  float: left !important;
  width: 80px;
}

.mission_credits{
  margin-left: 30px;
  margin-right: 30px;
}

.credits_input{
  position: relative;
  float: left;
  margin-left:0px !important;
  height: 40px !important;
}

::v-deep .credits_input .el-input__inner{
  margin-top: 0px;
  height:40px;
  font-size: 12px;
}

.name_item{
  margin-left:30px;
  margin-right:30px;
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

.profile {
  height: 28px;
  width: 28px;
  border-radius: 50%;
}

.dabao_body{
  width: 100%;
  height: 2050px;
  padding-bottom: 50px;
}

.dabao_title{
  width:100%;
  float:left;
}

.dabao_subtitle{
  width:90%;
  text-align: left;
  margin-left:5%;
  margin-right:5%;
  margin-top:12px;
  margin-bottom: 12px;
}


.dabao_content{
  width:85%;
  float:left;
  text-align: left;
  margin-left:10%;
}

.dabao_words{
  width:100%;
  float:left;
  margin-top: 10px;
  margin-bottom: 10px;
}

.dabao_subwords{
  margin-left:5%;
}
</style>