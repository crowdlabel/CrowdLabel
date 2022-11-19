<template>
  <div>
    <div class="top_nav">
      <div class="top_nav_trigger">
        <img src="../assets/label.png" alt="label" height="26">
        <h2 class="logo">CrowdLabel</h2>
      </div>
      <div class="page_title">
        <h3 class="title">我的积分</h3>
        <img src="../assets/notifications.svg" alt="label" height="24">
      </div>
      <div class="my_account">
        <img src="../assets/my_account.svg" alt="label" height="23">
      </div>
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
            <div class="search_bar">
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
      dialogVisible: false
    };
  },
  methods: {
    chooseType: function () {
      this.dialogVisible = true
    },
    senderType: function (){
      this.$router.push('/senderlogin')
      // axios.get('http://localhost:8002/senderlogin', {params:{
      //           username: this.username
      //           }
      //       }).then((res) => {
      //           console.log(res)
      //           this.$router.push({
      //               name: 'connected',
      //               params: {
      //               username: this.username,
      //               usage: res.data
      //               }
      //           })
      //           })
      //       .catch((error) => {
      //           console.log(error)
      //       })
    },
    receiverType: function () {
      this.$router.push('/receiverlogin')
    }
  }
}
</script>

<style scoped>
@import '@/assets/font/font.css';

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
    padding-left: 20px;
}
.page_title {
    align-items: center;
    box-sizing: border-box;
    cursor: pointer;
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
    display: flex;
    cursor: pointer;
    flex:1;
    justify-content: space-between;
    height: 100%;
}
.left_nav_list_top {
    box-sizing: border-box;
    list-style-type: none;
    flex: 1;
    flex-direction: column;
    margin: 0;
    padding: 12px;
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
}
.left_nav_list_item_active {
    background-color: rgba(84,47,238,.14);
    color: rgba(84,47,238,1);
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
    cursor: pointer;
    flex:1;
    height: calc(100vh - 50px);
}
.search_bar {
    box-sizing: border-box;
    flex-direction: row;
}

</style>