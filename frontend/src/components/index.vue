<template>
    <div class="layout">
        <Menu mode="horizontal" theme="dark" activeName="1">
            <h2 class="layout-logo">员工培训</h2>
            <div class="layout-nav">
                <Menu-item name="1" class="titleDirection" @click.native="title = '首页'">
                    <Icon type="home"></Icon>
                    <router-link to="/" class="routerfont">首页</router-link>
                </Menu-item>
                <Menu-item name="2" @click.native="learnAndTraining()"  v-if="user.user_id" class="titleDirection2">
                    <Icon type="ios-book"></Icon>
                    <router-link to="/learn" class="routerfont">学习培训</router-link>
                </Menu-item>
                <Menu-item name="3" @click.native="homework()"  v-if="user.user_id" class="titleDirection2">
                    <Icon type="ios-analytics"></Icon>
                    <router-link to="/homework" class="routerfont">作业</router-link>
                </Menu-item>
                <Submenu name="4" v-if="user.user_id" class="titleDirection2">
                    <template slot="title">
                        {{user.username}}
                    </template>
                        <Menu-item name="4-1" @click.native="title == '个人信息'">
                            <Icon type="ios-information"></Icon>
                            <router-link to="/personalInfo">个人信息</router-link>
                        </Menu-item>
                        <Menu-item name="4-2" @click.native="personalInfo = true"><Icon type="edit"></Icon>修改密码</Menu-item>
                        <Menu-item name="4-2" @click.native="quit"><Icon type="log-out"></Icon>退出登录</Menu-item>
                </Submenu>
                <Menu-item name="4" @click.native="loginModel = true" v-else style="left: 700px">
                    <Icon type="log-in"></Icon>
                    登录
                </Menu-item>
            </div>
        </Menu>
        <div class="layout-breadcrumb">
            <Breadcrumb>
                <Breadcrumb-item v-model="title">{{ title }}</Breadcrumb-item>
            </Breadcrumb>
        </div>
        <div class="layout-content">
            <router-view></router-view>
        </div>
        <div class="layout-copy">
            2011-2016 &copy; 某某公司formInline
        </div>
        <!--登录弹窗-->
        <Modal
            title="登录"
            :value.sync="loginModel"
            class-name="vertical-center-modal"
            @on-ok="login"
            @on-cancel="cancelLogin"
            okText="登录"
            width="250">
            <div class="loginForm">
                <i-input type="text" v-model="userInfo.user_id" placeholder="账号" size="large">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                </i-input>
                <i-input type="password" v-model="userInfo.password" placeholder="密码" size="large" style="padding-top:8px">
                    <Icon type="ios-locked-outline" slot="prepend"></Icon>
                </i-input>
            </div>
        </Modal>
        <!--修改密码弹窗-->
        <Modal
            title="修改密码"
            :value.sync="personalInfo"
            class-name="vertical-center-modal"
            @on-ok="login"
            @on-cancel="cancelLogin"
            okText="修改"
            width="250">
            <div class="loginForm">
                <i-input type="text" v-model="userInfo.user_id" placeholder="原密码" size="large">
                    <Icon type="ios-person-outline" slot="prepend"></Icon>
                </i-input>
                <i-input type="password" v-model="userInfo.password" placeholder="修改密码" size="large" style="padding-top:8px">
                    <Icon type="ios-locked-outline" slot="prepend"></Icon>
                </i-input>
            </div>
        </Modal>
    </div>
</template>
<script> 
    export default {
        data() {
            return {
                // 登录弹窗是否显示
                loginModel: false,
                // 登录临时存储用户名和密码
                userInfo: {
                    user_id: '',
                    password: ''
                },
                // 存储验证登录之后用户所有信息
                user: [],
                title:'首页',
                personalInfo: false
            }
        },
        methods: {
            learnAndTraining() {
                if (this.user == null)
                    alert('未登录不能查看'); 
                this.title = '学习培训'
            },
            homework() {
                if (this.user == null)
                    alert('未登录不能查看'); 
                this.title = '作业';
            },
            // 登录弹窗回调
            login() {
                this.loginModel = false;
                    this.$http.get('/api/user/'+this.userInfo.user_id).then(res=>{
                        this.user = res.data.results[0];
                        if (this.userInfo.user_id == this.user.user_id && this.userInfo.password == this.user.user_password) {
                            var titleDirection = document.getElementsByClassName('titleDirection')
                            // 动态改变home的位置
                            titleDirection[0].style.left = "484px";
                            this.$Message.info('登录成功');
                            this.$router.push('/');
                        }else{
                            this.user = []
                            alert('登录失败请重新登录');
                        }                        
                    });
                                        
            },
            cancelLogin() {
                this.loginModel = false;
                console.log(1);
            },
            // 退出登录
            quit() {
                this.user = {};
                var titleDirection = document.getElementsByClassName('titleDirection')
                // 动态改变home的位置
                titleDirection[0].style.left = "700px";
                this.$Message.info('退出成功');
                this.$route.push('/');
            }
        }
    }
</script>
<style>
    .layout{
        position: relative;
        border: 0px solid #d7dde4;
        background: #f5f7f9;
    }
    .layout-logo{
        width: 100px;
        height: 30px;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 0px;
        left: 20px;
    }
    .layout-nav{
        width: 420px;
        margin: 0 auto;
    }
    .layout-assistant{
        width: 300px;
        margin: 0 auto;
        height: inherit;
    }
    .layout-breadcrumb{
        padding: 10px 15px 0;
    }
    .layout-content{
        min-height: 818px;
        margin: 10px;
        overflow: hidden;
        background: #fff;
        border-radius: 4px;
    }
    .layout-content-main{
        padding: 10px;
    }
    .layout-copy{
        text-align: center;
        padding: 10px 0 20px;
        color: #9ea7b4;
        bottom: 0;
    }
    /*路由字体颜色*/
    .routerfont{
        color: #9ea7b4;
    }
    /*登录显示*/
    .vertical-center-modal{
        display: flex;
        align-items: center;
        justify-content: center;    
    }
    .vertical-center-modal .ivu-modal{
        top: 0;
    }
    /*登录窗口*/
    .loginForm{
        position: relative;
        /*margin: 10px;*/
    }
    /*导航栏位置*/
    .titleDirection{
        position: relative;
        left: 700px;
    }
    .titleDirection2{
        position: relative;
        left: 484px;
    }
</style>