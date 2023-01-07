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
                            <el-form :model="loginRuleForm" status-icon :rules="loginRules" ref="loginRuleForm" label-width="100px" class="demo-ruleForm">
                                <el-form-item prop="loginname">
                                    <el-input placeholder="请输入用户名" v-model="loginRuleForm.loginname" id="loginusername" autocomplete="off"></el-input>
                                </el-form-item>
                    
                                <el-form-item prop="loginpass">
                                    <el-input placeholder="请输入密码" type="password" v-model="loginRuleForm.loginpass" id="loginpassword" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="submitLogin('loginRuleForm')">登录</el-button>
                                    <el-button @click="backToMain()">返回</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </el-tab-pane>
                    <el-tab-pane label="注册" name="second">
                        <div class="center_form">
                            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                                <el-form-item prop="name">
                                    <el-input placeholder="请输入用户名" v-model="ruleForm.name" autocomplete="off" id="registername"></el-input>
                                </el-form-item>
                                <el-form-item prop="pass">
                                    <el-input placeholder="请输入密码" type="password" v-model="ruleForm.pass" id="registerpassword" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item prop="checkPass">
                                    <el-input placeholder="请确认密码" type="password" v-model="ruleForm.checkPass" id="registerpassword2" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item prop="email">
                                    <el-input placeholder="请输入邮箱地址" v-model="ruleForm.email" id="registeremail" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item prop="verif">
                                    <div class="verify_code">
                                        <el-input placeholder="请输入验证码" autocomplete="off" v-model="ruleForm.verif" class="input_verify" id="registerverification"></el-input>
                                        <el-button :disabled="disable" class="button_verify" @click="verifyEmailbtn()">{{text}}</el-button>
                                    </div>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="submitRegister('ruleForm')">注册</el-button>
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

import { ApiClient } from '@/crowdlabel-api/src';
import { UsersApi } from '@/crowdlabel-api/src';
import { AuthApi } from '@/crowdlabel-api/src';
import { mapMutations } from 'vuex';

export default {
    
    data () {
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
            if (!/^[\x21-\x7e]{8,64}$/.test(value)) {
                callback(new Error('密码格式错误:请输入8-64位密码'));
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
            callback(new Error('请输入用户名'));
            } else {
                if (!/^[\x21-\x7e]{3,64}$/.test(value)) {
                    callback(new Error('用户名格式错误:请输入3-64位用户名'));
                } else {
                    let ready_username = document.getElementById('registername').value;
                    this.user.availabilityUsersAvailabilityPut({'username': ready_username},
                    (error, data, response) => {
                        if (!data['username']){
                            callback(new Error('用户名已被占用'));
                            } else {
                                callback();
                            }
                        }
                    );
                }
            }
        };
        var validateEmail = (rule, value, callback) => {
            if (value === '') {
            callback(new Error('请输入邮箱'));
            } else {
                let mailReg = /^([a-zA-Z0-9_-]+(.[a-zA-Z0-9])?)@([a-zA-Z0-9_-]+)((.[a-zA-Z0-9_-]+)+)$/
                if (!mailReg.test(value)){
                    callback(new Error('邮箱格式错误'));
                } else {
                    this.disable = false;
                    let ready_email = document.getElementById('registeremail').value;
                    this.user.availabilityUsersAvailabilityPut({'email': ready_email},
                    (error, data, response) => {
                        if (response.status == 422){
                            callback(new Error('邮箱格式错误'));
                        } else if (!data['email']){
                            callback(new Error('邮箱已被占用'));
                        } else  {
                            this.disable = false;
                            callback();
                        }
                    }
                    );
                }
            }
        };
        var validateLoginName = (rule, value, callback) => {
            if (value===''){
                callback(new Error('请输入用户名'));
            } else {
                callback();
            }
        };
        var validateLoginPass = (rule, value, callback) => {
            if (value===''){
                callback(new Error('请输入密码'))
            } else {
                callback();
            }
        };
        var validateVerif = (rule, value, callback) => {
            if (value === ''){
                callback(new Error('请输入验证码'))
            } else {
                let veriReg = /^[0-9]{6}$/
                if (!veriReg.test(value)){
                    callback(new Error('验证码格式错误'))
                }
                else {
                    callback();
                }

            }
        };
        return {
            text: "发送验证码",
            time: 60,
            timer: null,
            disable: true,
            activeName: 'second',
            client: '',
            auth: '',
            user: '',
            ruleForm: {
                name: '',
                pass: '',
                checkPass: '',
                email: '',
                verif: ''
            },
            loginRuleForm: {
                loginname: '',
                loginpass: ''
            },
            loginRules: {
                loginpass: [
                    { validator: validateLoginPass, trigger: 'blur'}
                ],
                loginname: [
                    { validator: validateLoginName, trigger: 'blur'}
                ]
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
                    { validator: validateEmail, trigger: 'change'}
                ],
                verif: [
                    { validator: validateVerif, trigger: 'blur' }

                ]
            }
        };
    },
    created () {
        const time = localStorage.getItem('time');
        if (time && time>0) {
            this.text = time + "s后重新发送"
            this.time = time
            this.verifyEmailbtn();
        }
        
    },
    mounted() {
        let base = this.$root.basePath
        console.log(base)
        var apiClient = new ApiClient(base);
        this.client = apiClient
        var usersApi = new UsersApi(apiClient);
        this.user = usersApi
        var authApi = new AuthApi(apiClient);
        this.auth = authApi
    },
    methods: {
        ...mapMutations(['changeLogin']),
        handleTabClick(tab, event){
            console.log(tab, event)
        },
        submitRegister(formName) {
            this.$refs[formName].validate((valid) => {
            if (valid) {
                let ready_username = document.getElementById('registername').value;
                let ready_password = document.getElementById('registerpassword').value;
                let ready_email = document.getElementById('registeremail').value;
                let ready_verification = document.getElementById('registerverification').value
                this.user.registerUsersRegisterPost({
                    "username": ready_username,
                    "password": ready_password,
                    "email": ready_email,
                    "user_type": "requester",
                    "verification_code": ready_verification
                    },
                    (error, data, response) => {
                        console.log(error, data, response);
                    });
                // alert('successfully registered!');
                this.activeName = "first"
            } else {
                console.log('注册出错!!');
                return false;
            }
            });
        },
        submitLogin(formName) {
            let _this = this;
            this.$refs[formName].validate((valid) => {
            if (valid) {
                let ready_login_username = document.getElementById('loginusername').value;
                let ready_login_password = document.getElementById('loginpassword').value;
                this.auth.loginLoginPost(ready_login_username, ready_login_password, {}, 
                    (error, data, response) => {
                        if (response.status == 200){
                            let token = data["access_token"];
                            _this.$store.commit('changeLogin', token);
                            this.$router.push({
                                path: '/sendermission',
                            });
                        } else {
                            alert('用户名错误或者密码错误!')
                        }
                    });
            } else {
                console.log('请输入用户名或者密码');
                return false;
            }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        backToMain: function (){
            this.$router.push('/');
        },
        verifyEmailbtn () {
            this.disable=true
            let ready_email = document.getElementById('registeremail').value
            console.log(ready_email);
            this.user.verifyEmailUsersVerifyEmailPost({
                "email": ready_email
            });
            this.text = this.time + "s后重新发送"
            localStorage.setItem('time', this.time)
            this.timer = setInterval(() => {
                if (this.time > 0) {
                    this.time--
                    localStorage.setItem('time', this.time)
                    this.text = this.time + "s后重新发送"
                } else {
                    clearInterval(this.timer);
                    this.time = 60
                    this.disable = false
                    this.text = '发送验证码'
                }
            }, 1000)
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
    left:35%;
    width:30%;
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
.verify_code{
    position: relative;
    display:inline-block;
    width:80%;
}
::v-deep .el-form-item__error {
    left: 10%;
}
::v-deep .button_verify{
    width:50% !important;
    float: right;
}
::v-deep .input_verify{
    width:50% !important;
    float: left;
}

::v-deep .el-input__inner:focus{
    border-color: #5D3BE6;
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
    margin-bottom: 0px !important;
    width:100%;
    line-height: 0px;

}
::v-deep .el-input{
    width: 80%;
}
::v-deep .el-button--primary{
    width:80%;
    background-color: #5D3BE6;
    border-color: #5D3BE6;
    margin-top: 0px;
    margin-bottom: 20px !important;
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
    margin-bottom: 18px !important;
}
::v-deep .el-button--default.is-disabled:hover{
    color: #C0C4CC;
    background-color: #FFF;
    border-color: #EBEEF5;
}

::v-deep .el-button--primary.is-disabled, .el-button--primary.is-disabled:hover{
    color: #C0C4CC;
    background-color: #FFF;
    border-color: #EBEEF5;
}


.login_logo{
    position:relative;
    top: 10px;
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
