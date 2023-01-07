<template>
  <div class="all">
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">我的积分</h3>
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
                    <a aria-current="page" class="left_nav_list_item left_nav_list_item_active" data-external="true" href="/credits">
                        <img src="../assets/credits_active.png" height="19" width="20">
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
          <h3 class="sub_title">数据概览</h3>
          <div class="row">
            <div class="box_overview">
              <p class="box_title">近7日收入</p>
              <div class="box_credits">
                <p class="box_number">{{ credits_last_week }}</p>
                <p class="box_unit">积分</p>
              </div> 
            </div>
            <div class="box_overview">
              <p class="box_title">累计总收入</p>
              <div class="box_credits">
                <p class="box_number">{{credits_total}}</p>
                <p class="box_unit">积分</p>
              </div>
            </div>
          </div>
          <h3 class="sub_title">积分提现</h3>
          <div class="row">
            <div class="box_pay">
              <p class="box_title">微信 ></p>
              <img src="../assets/wechat.png" height="100px">
            </div>
            <div class="box_pay">
              <p class="box_title">支付宝 ></p>
              <img class="img_alipay" src="../assets/alipay.png" height="85px">
            </div>
            <div class="box_pay">
              <p class="box_title">银行卡 ></p>
              <img class="img_credit_card" src="../assets/credit_card.png" height="70px">
            </div>
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
// import { AuthApi } from '@/crowdlabel-api/src';

export default {
  data() {
    return {
      client: '',
      username: '',
      credits_last_week: '',
      credits_total: ''
    };
  },
  mounted() {
      let self = this
      let base = this.$root.basePath
      var apiClient  = new ApiClient(base);
      apiClient.authentications['OAuth2PasswordBearer'].accessToken = localStorage.getItem('Authorization')
      self.client = apiClient
      var usersApi = new UsersApi(apiClient);
      self.user = usersApi
      self.user.getMeUsersMeGet((error, data, response) => {
        console.log(response)
        if (error == 'Error: Unauthorized') {
          localStorage.removeItem('Authorization');
          this.$router.push('/receiverlogin');
        }
        self.username = response.body['username']
        self.credits_last_week = response.body['credits']
        self.credits_total = response.body['credits']
        console.log('credits_total: ' + self.credits_total)
      })
  },
  methods: {
    
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

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
}
.search_bar {
    box-sizing: border-box;
    flex-direction: row;
}

.sub_title{
  vertical-align: middle;
  text-align: left;
  font-size: 18px;
  font-weight: bold;
  color:black;
  margin-left: 50px;
  margin-top: 30px;
}
.row {
  box-sizing: border-box;
  flex-direction: row;
  position: relative;
  display: flex;
  margin-left: 70px;
  margin-bottom: 20px;
}
.box_overview{
  background: rgba(84,47,238,.05);
  margin: 10px 0px 0px 30px;
	padding: 10px;
	width: 355px;
	height: 220px;
	border-radius: 8px;
	font-size: 14px;
}
.box_title {
  text-align: left;
  margin-left: 15px;
  font-size: 15px;
  color: rgba(0,0,0,0.7);
}
.box_credits {
  box-sizing: border-box;
  flex-direction: row;
  position: relative;
  display: flex;
  margin-left: 60px;
  line-height: 50px;
  vertical-align: middle;
}
.box_number {
  text-align: left;
  vertical-align: text-bottom;
  font-size: 45px;
  margin: 0px 0px 0px 0px;
  color: rgba(84,47,238,1);
  font-weight: bold;
}
.box_unit {
  text-align: left;
  vertical-align: sub;
  font-size: 16px;
  margin: 0px 0px 0px 6px;
  color: rgba(0,0,0,1);
  padding-top: 7px;
}

.box_pay{
  background: rgba(0,0,0,.03);
  margin: 10px 0px 0px 20px;
	padding: 10px;
	width: 230px;
	height: 190px;
	border-radius: 8px;
	font-size: 14px;
  cursor: pointer;
}

.img_alipay {
  margin-top: 5px;
}
.img_credit_card {
  margin-top: 10px;
}

</style>