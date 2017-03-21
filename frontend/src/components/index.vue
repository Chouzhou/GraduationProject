<template>
    <div class="layout">
        <Menu mode="horizontal" theme="dark" activeName="1">
            <h2 class="layout-logo">员工培训</h2>
            <div class="layout-nav">
                <Menu-item name="1">
                    <Icon type="home"></Icon>
                    <router-link to="/" class="routerfont">首页</router-link>
                </Menu-item>
                <Menu-item name="2" @click.native="learnAndTraining()">
                    <Icon type="ios-book"></Icon>
                    <router-link to="/learn" class="routerfont">学习培训</router-link>
                </Menu-item>
                <Menu-item name="3">
                    <Icon type="ios-analytics"></Icon>
                    <router-link to="#" class="routerfont">考试</router-link>
                </Menu-item>
                <Submenu name="4" v-if="user">
                    <template slot="title">
                        
                        {{user}}
                    </template>
                        <Menu-item name="4-1">
                            <Icon type="ios-information"></Icon>
                            <router-link to="/personalInfo">个人信息</router-link>
                        </Menu-item>
                        <Menu-item name="4-2"><Icon type="edit"></Icon>修改密码</Menu-item>
                        <Menu-item name="4-2"><Icon type="log-out"></Icon>退出登录</Menu-item>
                </Submenu>
                <Menu-item name="4" @click.native="loginModel = true" v-else>
                    <Icon type="log-in"></Icon>
                    登录
                     <!--<i-button >登录</i-button>-->
                    <!--<router-link to="#" class="routerfont">登录</router-link>-->
                </Menu-item>
                <Modal
                    title="对话框标题"
                    :value.sync="loginModel"
                    class-name="vertical-center-modal"
                    @on-ok="login"
                    @on-cancel="cancelLogin">
                    <p>对话框内容</p>
                    <p>对话框内容</p>
                    <p>对话框内容</p>
                </Modal>
            </div>
        </Menu>
        <div class="layout-breadcrumb">
            <Breadcrumb>
                <Breadcrumb-item href="/">首页</Breadcrumb-item>
            </Breadcrumb>
        </div>
        <div class="layout-content">
            <router-view></router-view>
        </div>
        <div class="layout-copy">
            2011-2016 &copy; 某某公司
        </div>
    </div>
</template>
<script> 
    export default {
        data() {
            return {
                user: '',
                loginModel: false
            }
        },
        methods: {
            learnAndTraining() {
                console.log(1);
            },
            // 登录弹窗回调
            login() {
                this.loginModel = false;
                console.log(1);
                this.user = 'jack';
                this.$router.push('/');
            },
            cancelLogin() {
                this.loginModel = false;
                console.log(1);
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
        /*background: #5b6270;*/
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
</style>