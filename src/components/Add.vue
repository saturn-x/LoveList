<template>
    <div>
    <a-modal
      v-model="myVisible"
      :title="headr"
      @ok="submitModal"
      @cancel="cancelModal"
      ok-text="确认"
      cancel-text="取消" 
    >

        <div>
            <a-collapse default-active-key="1" :bordered="false">
            <template #expandIcon="props">
                <a-icon type="caret-right" :rotate="props.isActive ? 90 : 0" />
            </template>
            <a-collapse-panel key="1" header="日常" :style="customStyle">
                <div v-for="(item,index) in dailylist" :key="index" >
                    <a-tag color="green"  >
                        {{item.id}}、{{item.name}}
                    </a-tag>
                    <a-badge :count="dailysocre[index]"  :number-style="{ backgroundColor: '#52c41a' }" show-zero />
                    <a-slider :marks="item.mark" :default-value="0" :max="item.max"  :step="null" @change="changeclick(),onclick(index)" @afterChange="change" />
                </div>
            </a-collapse-panel>
            <a-collapse-panel key="2" header="特殊" :style="customStyle">
                <div v-for="(item,index) in speciallist" :key="index" >
                    <a-tag color="green"  >
                        {{item.id}}、{{item.name}}
                    </a-tag>
                    <a-badge :count="specialsocre[index]"  :number-style="{ backgroundColor: '#52c41a' }" show-zero />
                    <a-slider :marks="item.mark" :default-value="0" :max="item.max"  :step="null" @change="onclick(index)" @afterChange="change" />
                </div>
            </a-collapse-panel>
            </a-collapse>
        </div>
    </a-modal>
    </div>
</template>

<script>

export default {

    name:'Add',
    props: {
        visible: Boolean,
        date:""
    },
    data() {
        return {
            //模态框标题
            headr:"",
            foucusid:0,
            foucusvalue:0,
            focusdaily:false,
            dailylist:Object,
            dailysocre:[],
            speciallist:Object,
            specialsocre:[],
            marks1:{
                0:"0",
                100:"100"
            },
            myVisible: this.visible,
            customStyle:
                'background: #f7f7f7;border-radius: 4px;margin-bottom: 24px;border: 0;overflow: hidden',
        };
    },
    beforeMount(){
        this.$http.get('/sql_dailylist').then(request =>{
                // console.log(request.data)
                this.dailylist=request.data
          }).catch(err=>{
            console.log('接收数据error')
        })
        this.$http.post('/sql_specialist',{
            name:this.$route.params.name
        }).then(request =>{
                console.log("特殊的请求")
                console.log(request.data)
                this.speciallist=request.data
          }).catch(err=>{
            console.log('接收数据error')
        })
    },

    methods: {
        changeclick:function(){
            this.focusdaily=true
        },
        onclick:function(index){
            this.foucusid=index
        },
        change:function(val){
            this.foucusvalue=val
        },
        submitModal(){
            console.log('点击确认')
            this.myVisible=!this.myVisible;
            //发送添加请求 遍历dailysocre
            let pre_add_info=[]
            for(var i in this.dailylist){
                if(this.dailysocre[i]!=0){
                    let tmp={}
                    tmp["id"]=this.dailylist[i].id
                    tmp["score"]=this.dailysocre[i]
                    tmp["daily"]=true
                    tmp["name"]=this.$route.params.name;
                    tmp["date"]=this.date
                    pre_add_info.push(tmp)
                }
            }
            for(var i in this.specialsocre){
                if(this.specialsocre[i]!=0){
                    let tmp={}
                    tmp["id"]=this.speciallist[i].id
                    tmp["score"]=this.specialsocre[i]
                    tmp["daily"]=false
                    tmp["name"]=this.$route.params.name;
                    tmp["date"]=this.date
                    pre_add_info.push(tmp)
                }
            }
            console.log("提交请求")
            console.log(pre_add_info)
            //发送请求
            this.$http.post('/add_record',{
                params:pre_add_info
            }).then(request =>{
                console.log("添加成功")
                this.$router.go(0)
            }).catch(err=>{
                console.log('sql_name接收数据error')
            })
            // location.reload()
        },
        cancelModal(){
            console.log('点击取消')
            this.myVisible=!this.myVisible
        },
    },
    watch:{
            myVisible: function (val) {
                    this.$emit('update:visible', val)
            },
            visible: function (val) {
                this.myVisible = val
                this.headr="选中的日期："+this.date
            },
            dailylist:function(dailylist){
                for(var i in dailylist){
                    //添加mark
                    let mark={}
                    for(var j=0;j<=dailylist[i]["max"];j+=dailylist[i]["step"]){
                        mark[j]=j+"";
                    }
                    dailylist[i]["mark"]=mark;
                    this.dailysocre.push(0);
                }
            },
            speciallist:function(speciallist){
                for(var i in speciallist){
                    //添加mark
                    let mark={}
                    for(var j=0;j<=speciallist[i]["max"];j+=speciallist[i]["step"]){
                        mark[j]=j+"";
                    }
                    speciallist[i]["mark"]=mark;
                    this. specialsocre.push(0);
                }
            },
            foucusvalue:function(){
                if(this.focusdaily){
                    this.dailysocre[this.foucusid]=this.foucusvalue;
                    this.dailysocre = this.dailysocre.slice(0)
                }else{
                    this.specialsocre[this.foucusid]=this.foucusvalue;
                    this.specialsocre = this.specialsocre.slice(0)
                }
                console.log(this.dailysocre)
                console.log(this.specialsocre)
                this.focusdaily=false
            },
            foucusid:function(){
                if(this.focusdaily){
                    this.dailysocre[this.foucusid]=this.foucusvalue;
                    this.dailysocre = this.dailysocre.slice(0)
                }else{
                    this.specialsocre[this.foucusid]=this.foucusvalue;
                    this.specialsocre = this.specialsocre.slice(0)
                }

            }

    }

}
</script>