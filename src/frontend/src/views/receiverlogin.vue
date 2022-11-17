<template>
    <div class="whole">
        <div class="logo_mid">
            <img src="../assets/login_logo.png" class="login_logo">
        </div>
        <div class="bar_mid">
            <div class="select_bar_mid">
                <el-tabs stretch v-model="activeName" @tab-click="handleTabClick">
                    <el-tab-pane label="登录" name="first">
                        <div class="center_form">
                            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                                <el-form-item prop="name">
                                    <el-input placeholder="请输入用户名" type="" v-model="ruleForm.checkUsername" autocomplete="off"></el-input>
                                </el-form-item>
                    
                                <el-form-item prop="pass">
                                    <el-input placeholder="请输入密码" type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="submitLogin('ruleForm')">确认</el-button>
                                    <el-button @click="backToMain()">返回</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </el-tab-pane>
                    <el-tab-pane label="注册" name="second">
                        <div class="center_form">
                            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                                <el-form-item prop="name">
                                    <el-input placeholder="请输入用户名" type="" v-model="ruleForm.checkUsername" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item prop="pass">
                                    <el-input placeholder="请输入密码" type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item prop="checkPass">
                                    <el-input placeholder="请确认密码" type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item prop="email">
                                    <el-input placeholder="请输入邮箱地址" type="email"></el-input>
                                    <el-button class="button_verify" @click="verifyEmail()">验证</el-button>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="submitRegister('ruleForm')">提交</el-button>
                                    <el-button @click="backToMain()">返回</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </el-tab-pane>
                </el-tabs>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                callback(new Error('请输入密码'));
                } else {
                if (this.ruleForm.checkPass !== '') {
                    this.$refs.ruleForm.validateField('checkPass');
                }
                callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                callback(new Error('请再次输入密码'));
                } else if (value !== this.ruleForm.pass) {
                callback(new Error('两次输入密码不一致!'));
                } else {
                callback();
                }
            };
            var validateName = (rule, value, callback) => {
                if (value === '') {
                callback(new Error('请再次输入用户名'));
                } else {
                callback();
                }
            };
            var validateEmail = (rule, value, callback) => {
                if (value === '') {
                callback(new Error('请输入邮箱'));
                } else {
                callback();
                }
            };
            return {
                activeName: 'second',
                ruleForm: {
                    pass: '',
                    checkPass: '',
                },
                rules: {
                    name: [
                        { validator: validateName, trigger: 'blur'}
                    ],
                    pass: [
                        { validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        { validator: validatePass2, trigger: 'blur' }
                    ],
                    email : [
                        { validator: validateEmail, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            handleTabClick(tab, event){
                console.log(tab, event)
            },
            submitRegister(formName) {
                this.$refs[formName].validate((valid) => {
                if (valid) {
                    alert('registered!');
                } else {
                    console.log('error registration!!');
                    return false;
                }
                });
            },
            submitLogin(formName) {
                this.$refs[formName].validate((valid) => {
                if (valid) {
                    alert('logging in...');
                } else {
                    console.log('error username or password');
                    return false;
                }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            backToMain: function (){
                this.$router.push('/')
            },
        }
    };
</script>

<style scoped>
@import '@/assets/font/font.css';
.whole{
    border-style: solid;
    border-radius: 20px;
    border-color: #5D3BE6;
    top:10%;
    left:28%;
    width:44%;
    position:absolute;
    height: 600px;
    display: flex;
    flex-direction: column;
    min-width: 400px;
}
.logo_mid{
    position:relative;
    left:0%;
    height: 100px;
    width: 100%;
}
::v-deep .button_verify{
    position:absolute;
    top: 0px;
    left: 90%;
    width:10% !important;
    padding-left:0px !important;
    padding-right:0px !important;
}
::v-deep .el-tabs__header{
    margin-left:auto;
    margin-right:auto;
    width:70%;
    margin-bottom:30px;
}
::v-deep .el-tabs__active-bar{
    background-color:#6729B6;
}
::v-deep .el-tabs__item:hover{
    color: #6729B6;
}
::v-deep .el-tabs__item.is-active{
    color:#6729B6;
}
::v-deep .el-tabs__item{
    font-size: 18px;
}
::v-deep .el-form-item__content{
    margin-left:0px !important;
    margin-bottom: 5px !important;
    width:100%;
}
::v-deep .el-input{
    width: 80%;
}
::v-deep .el-button--primary{
    width:80%;
    background-color: #5D3BE6;
    border-color: #5D3BE6;
    margin-top: 30px;
    margin-bottom: 20px;
}
::v-deep .el-button--default{
    width:80%;
    margin-left: 0px !important;
}
::v-deep .el-button.el-button--primary:focus, .el-button.el-button--primary:hover{
    background:#3C1C66;
    border-color: #3C1C66;
}
::v-deep .el-button.el-button--default:focus, .el-button.el-button--default:hover{
    color: #5D3BE6;
    background-color: #F3EAFF;
}
::v-deep .el-form-item.el-form-item--feedback{
    display: flex;
}
.login_logo{
    position:relative;
    top: 30px;
    width: 70%;
}
.bar_mid{
    position:relative;
    margin-right:0px !important;
    left:10%;
    height:500px;
    width: 80%;
}
.select_bar_mid{
    position:relative;
    height:450px;
}
</style>