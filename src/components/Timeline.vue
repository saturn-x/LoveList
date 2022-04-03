<template>
    <div>
        <br>
        <a-progress
        type="circle"
        :stroke-color="{
            '0%': '#108ee9',
            '100%': '#87d068',
        }"
        :percent="100"
        />
        <br><br><br>
        <a-timeline v-for="(item,index) in myinfo" :key="index">
            <a-timeline-item>{{item.name}}  <a-tag color="#87d068">{{item.score}}分</a-tag>
                <a-button type="danger" shape="circle" icon="close" :size="size" class="close-btn" @click="single_delete(item.id,index)" />
            </a-timeline-item>
        </a-timeline>
        <a-button type="primary" block @click="changemodel">
            添加
        </a-button>
        <add :visible.sync="keyDialogVisible" :date="date"  @renderall="renderall"/>
    </div>
</template>
<script>
import Add from './Add.vue'

export default {
    components: { Add },
    name:'Timeline',
    props:['info','selectdate'],

    data:function(){
        return{
            keyDialogVisible: false,
            size:"small",
            myinfo:[],
            //选中的日期
            date:""
        }
    },
    methods:{
        changemodel:function(){
            this.keyDialogVisible=!this.keyDialogVisible
        },
        single_delete:function(id,index){
            console.log("id:"+id)
            this.myinfo.splice(this.myinfo.indexOf(this.myinfo),index+1);
            let pre_delete_info={}
            pre_delete_info["id"]=id
            pre_delete_info["name"]=this.$route.params.name;
            //将id name传过去即可
            this.$http.post('/delete_record',{
                params:pre_delete_info
            }).then(request =>{
                alert("删除成功！")
            }).catch(err=>{
                console.log('删除error')
            })


       
        },
        renderall:function(){
            this.$emit("renderall")
        }
        
    },
    watch:{
            //传入的数据进行传给myinfo
            info:function(info){
                console.log("哈哈哈哈")
                this.myinfo=info
                this.date=this.selectdate
            },
        }
}




</script>
<style>
.close-btn{
    float: right;
}
</style>
