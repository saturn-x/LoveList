<template>
    <div> 
            <!-- <router-view v-if="showState" />   -->
            <a-layout id="components-layout-demo-top" class="layout">
                <a-layout-header id="header">
                    <h1 id="head-text">在一起：<span>{{date}}</span></h1>
                </a-layout-header>
                <a-layout-content style="padding: 0 50px">
                <a-breadcrumb style="margin: 16px 0">

                </a-breadcrumb>
                <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
                        <a-tag color="orange">
                             {{name}}
                        </a-tag>
                        <a-tag color="green">
                            总分：{{allscore}}分
                        </a-tag>
                        <br><br><br>
                        <a-date-picker :default-value="moment(today, dateFormat)" :format="dateFormat"  @change="onChange"/>
                        <timeline :info.sync="selectinfo" :selectdate="selectdate" @renderall="renderall" />
                </div>
                </a-layout-content>
            <a-layout-footer style="text-align: center">
               WYJ IS A <strong>PIG</strong>
            </a-layout-footer>
        </a-layout>
    </div>
</template>
<script>
import moment from 'moment';
import 'moment/locale/zh-cn';
import Timeline from './Timeline.vue';
export default {
    name:'Index',
    components: {
        Timeline
    },
    created:function(){
        setInterval(this.timer,1000);
    },
    data:function(){
        return {
            name:'',
            date:'wait',
            dateFormat: 'YYYY-MM-DD',
            today:moment(),
            selectdate:'',
            selectinfo:[],
            selectscore:0,
            allinfo:Object,
            allscore:0,
            reload:this.reload
        }
    },
    methods:{
        //  reload(){
        //     this.showState = false;
        //     this.$nextTick(()=>{
        //         this.showState = true;
        //     })
        // },
        //修改日期
        onChange(date, dateString) {
            this.selectdate=dateString

        },
        timer(){
            var last=1609938000000;
            var time = new Date();
            let day=(time-last)/86400000
            let hour=(time-last)%86400000/3600000
            let min=(time-last)%3600000/60000
            let sec=(time-last)%60000/1000
            this.date=parseInt(day)+1+"日"+parseInt(hour)+"时"+parseInt(min)+"分"+parseInt(sec)+"秒"
        },
        moment,
        selectdate_info(selectdate){
            console.log(this.selectdate+"选择一次")
            this.selectinfo=[]
            for(var i in this.allinfo){
                if(selectdate===this.allinfo[i]["date"]){
                    this.selectinfo.push(this.allinfo[i])
                }
            }
        },
        renderall(){
            console.log("执行一次renderall")
            this.name=this.$route.params.name;
            this.selectdate=moment().format(this.dateFormat)
            //请求结果添加info上
            //        this.$http.post('/sql_specialist',{
            // name:this.$route.params.name
            this.$http.post('/sql_name',{
                name:this.$route.params.name
            }).then(request =>{
                console.log("sql_name请求成功")
                this.allinfo=request.data
            }).catch(err=>{
                console.log('sql_name接收数据error')
        })
        }
    },
    beforeMount(){
      this.renderall()
    },
    watch:{
        allinfo:function(val){
            for(var i in val){
                this.allscore+=val[i]["score"]
            }
            this.selectdate_info(this.selectdate)
        },
        selectdate:function(){
            this.selectdate_info(this.selectdate)
        }
    }
    
}

</script>
<style scoped>
#head-text{
    color:rgb(193, 160, 160);
}
#header{
    background-color: hsl(0, 8%, 95%);
}
</style>


