<template>
  <div class="all">
    <div class="top_nav">
      <div class="top_nav_trigger">
        <a aria-current="page" class="back_button" data-external="true" href="/projects">
          <img src="../assets/back.png" height="18" width="18">
            <p class="list_item_title">返回任务大厅</p>
        </a>
      </div>
      <div class="page_title">
        <h3 class="title">消息中心</h3>
      </div>
    </div>
    <div class="body">
        <div class="left_nav">
            <ul class="left_nav_list_top">
                <li>
                    <a aria-current="page" class="left_nav_list_item" data-external="true" href="/myaccount">
                        <img src="../assets/my_account_2.png" height="21" width="20">
                        <p class="list_item_title">个人信息</p>
                    </a>
                </li>
                <li>
                    <a aria-current="page" class="left_nav_list_item  left_nav_list_item_active" data-external="true" href="/history">
                        <img src="../assets/notifications_2_active.png" height="20" width="20">
                        <p class="list_item_title">消息中心</p>
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
            <div class="user_row">
              <img class="profile_pic" src="../assets/image_placeholder.png"/>
              <div class="user_column">
                <p class="username">用户名，</p>
                <p class="overview">您共有XX条新消息和XXX条历史消息。</p>
              </div>
            </div>
            <div class="scroll_view">
              <el-scrollbar style="height: 100%">
                <!-- 用于展示下拉，填充的内容 -->
                <div class="scroll_element">
                  <div class="scroll_element_text">
                    <p class="element_info">来自"XXX"任务的发布者 · 1小时前</p>
                    <h4 class="element_content">恭喜，你的XXX任务数据已通过审核，获得积分XXX。</h4>
                  </div>
                  <img src="../assets/image_placeholder.png" class="element_image"/>
                </div>
                <div class="scroll_element">
                  <div class="scroll_element_text">
                    <p class="element_info">来自CrowdLabel众包平台 · 5小时前</p>
                    <h4 class="element_content">测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试</h4>
                  </div>
                  <img src="../assets/image_placeholder.png" class="element_image"/>
                </div>
                <div class="scroll_element">
                  <div class="scroll_element_text">
                    <p class="element_info">来自CrowdLabel众包平台 · 5小时前</p>
                    <h4 class="element_content">测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试</h4>
                  </div>
                  <img src="../assets/image_placeholder.png" class="element_image"/>
                </div>
                <div class="scroll_element">
                  <div class="scroll_element_text">
                    <p class="element_info">来自"测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试"任务的发布者 · 23小时前</p>
                    <h4 class="element_content">恭喜，你的XXX任务数据已通过审核，获得积分XXX。</h4>
                  </div>
                  <img src="../assets/image_placeholder.png" class="element_image"/>
                </div>
                <div class="scroll_element">
                  <div class="scroll_element_text">
                    <p class="element_info">来自"XXX"任务的发布者 · 1天前</p>
                    <h4 class="element_content">恭喜，你的XXX任务数据已通过审核，获得积分XXX。</h4>
                  </div>
                  <img src="../assets/image_placeholder.png" class="element_image"/>
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
import axios from 'axios'
export default {
  data() {
    return {
      
    };
  },
  methods: {

  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

.all {
  min-width: 800px;
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
    cursor: pointer;
    display: flex;
    min-width: 230px;
    max-width: 230px;
    padding-left: 10px;
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
    flex-direction: row;
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
    min-height: 135px;
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
.left_nav_list_item_active:hover {
    background-color: rgba(0,0,0,.06);
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

.user_row {
  flex-direction: row;
  display: flex;
  padding-left: 50px;
  padding-top: 30px;
}
.profile_pic {
  height: 110px;
  width: 110px;
  border-radius: 50%;
}
.user_column {
  flex-direction: column;
  display: flex;
  align-self: center;
}
.username {
  text-align: left;
  font-size: 24px;
  font-weight: bold;
  color: #5D3BE6;
  margin: 0px 30px 10px 30px;
}
.overview {
  text-align: left;
  font-size: 18px;
  color: rgba(0,0,0,.9);
  margin: 0px 30px 10px 30px;
}

.scroll_view {
  border-top: 1.2px solid rgba(0,0,0,.1);
  margin-top: 20px;
  height: calc(100vh - 210px);
  min-height: 140px;
}

.scroll_element {
  height: fit-content;
  border-bottom: 1.2px solid rgba(0,0,0,.1);
  flex-direction: row;
  display: flex;
  padding: 20px 25px;
}

.scroll_element_text {
  margin: 0px 20px;
  flex-direction: column;
  display: flex;
  align-items: flex-start;
}
.element_info {
  text-align: left;
  margin: 5px 0px 10px 0px;
  font-size: 10px;
  color: rgba(0,0,0,.7);
}
.element_content {
  text-align: left;
  font-weight:normal;
  margin: 0px 0px 3px 0px;
}
.element_image {
  height: 87px;
  width: 100px;
  align-self:center;
  margin-left: auto;
  text-align: right;
  border-radius: 10%;
}

</style>