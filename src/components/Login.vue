<template>
    <div>
        <a-layout id="components-layout-demo-top" class="layout">
            <a-layout-header id="header">
                <h1 id="head-text">登陆界面</h1>
            </a-layout-header>
            <a-layout-content style="padding: 0 50px">
            <a-breadcrumb style="margin: 16px 0">

            </a-breadcrumb>
            <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
                <!-- 登录表单 -->
                <a-form>
                    <a-form-item>
                        <a-input
                            placeholder="账号"
                            type="text"
                            v-model="username"
                        >
                            <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
                        </a-input>
                    </a-form-item>
                    <a-form-item>
                        <a-input
                            type="password"
                            placeholder="密码"
                            v-model="password"
                        >
                            <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
                        </a-input>
                    </a-form-item>
                    <a-form-item>
                        <a-checkbox
                            v-model="is_remeber"
                        >
                           记住密码！
                        </a-checkbox>
                        <br>
                        <a-button type="primary" html-type="submit" class="login-form-button" @click="login">
                            登陆
                        </a-button>
                         </a-form-item>
                </a-form>
            </div>
            </a-layout-content>
            <a-layout-footer style="text-align: center">
               WYJ IS A <strong>PIG</strong>
            </a-layout-footer>
        </a-layout>
    </div>
</template>
<script>


export default {

    name:'Login',
    data:function(){
        return{
            username:"",
            password:"",
            is_remeber:false,
        }
    },
    methods:{
        login(){
            alert("点击登陆");
            alert(this.username+" "+this.password+" "+this.is_remeber);
        },
    },
   

    
    
  
    
}

</script>
<style scoped>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}
#head-text{
    color:rgb(193, 160, 160);
}
#header{
    background-color: hsl(0, 8%, 95%);
}
</style>