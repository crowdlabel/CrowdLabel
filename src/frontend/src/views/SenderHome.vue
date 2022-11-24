<template>
    <div class="whole">
        <el-container class="top_part">
            <div class="top_logo">
                <img src="../assets/label.png" alt="label" height="26">
                    <h2 class="logo">CrowdLabel</h2>
            </div>
            <div class="top">
                <div class="top_left">

                </div>
                <div class="top_right">

                </div>
            </div>
        </el-container>
        <el-container class="main_part">
            <el-aside width="150px" class="left_part">
                <div class="aside_nav">
                    <el-menu
                        default-active="1"
                        class="nav_bar"
                        @open="handleOpen"
                        @close="handleClose">
                        <el-menu-item index="1">
                            <div class="nav_option">
                                <i class="el-icon-folder-opened"></i>
                                <span slot="title">我的任务</span>
                            </div>
                        </el-menu-item>
                        <el-menu-item index="2">
                            <div class="nav_option">
                                <i class="el-icon-coin"></i>
                                <span slot="title">我的积分</span>
                            </div>
                        </el-menu-item>
                    </el-menu>
                </div>
                <div clas="aside_bottom">

                </div>
            </el-aside>
            <el-main>
                MAIN
            </el-main>
        </el-container>
    </div>
</template>

<script> 
    export default {
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>

<style scoped>
body{
  padding-right: 0px !important;
  margin-top: 0px !important;
  margin-bottom: 0px !important;
  margin-left: 0px !important;
  margin-right: 0px !important;
}
.whole{
    width: 100%;
}
.top_logo {
    align-items: center;
    box-shadow: 1.2px 0 0 0 rgb(0 0 0 / 10%);
    box-sizing: border-box;
    display: flex;
    min-width: 230px;
    max-width: 230px;
    padding-left: 20px;
}
.logo{
  vertical-align: middle;
  text-align: left;
  font-family: 'Lobster';
  font-size: 22px;
  color:black;
  padding: 8px;
}
.left_part{
    min-width: 230px;
    max-width: 230px;
    height: 400px;
}
</style>