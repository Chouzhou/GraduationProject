<template>
    <div class="container" v-if="allHomeWork">
        <div v-if="allHomeWork != []">
        <div class="hwtag">
            <Tag type="dot" color="blue" @click.native="allHomeWork()">所有作业</Tag>
            <Tag type="dot" color="green" @click.native="doHomeWork()">完成作业</Tag>
            <Tag type="dot" color="red" @click.native="notDoHomeWork()">未完成作业</Tag>
        </div>
        <div class="hwcord">
            <Row>
                <i-col span="8" @click.native="submitHome()">
                    <Card>
                        <p slot="title">作业标题</p>
                        <p>作业要求</p>
                        <!--<p>卡片内容</p>
                        <p>卡片内容</p>-->
                    </Card>
                </i-col>
            </Row>
        </div>
        </div>
        <p v-else>还未有作业</p>
        <!--写作业弹窗-->
        <Modal
            title="写作业"
            :value.sync="submitModel"
            class-name="vertical-center-modal"
            @on-ok="submit"
            @on-cancel="cancelSubmit"
            okText="提交"
            class="hwForm">
            <div >
                 <Input v-model="homework" type="textarea" :autosize="{minRows: 10,maxRows: 20}" placeholder="请输入..." size="large"></Input>
            </div>
        </Modal>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                allHomeWork: [],
                submitModel: false,
                homework: ''
            }
        },
        methods: {
            allHomeWork() {
                alert('成功');
            },
            doHomeWork() {
                alert('成功');
            },
            notDoHomeWork() {
                alert('成功');
            },
            submit() {
                this.submitModel = false;
            },
            submitHome() {
                this.submitModel = true; 
            },
            cancelSubmit() {
                this.submitModel = false;
            }
        }
    }
</script>
<style>
.container{
    position: relative;
    width: 80%;
}
.hwtag{
    position: relative;
}
.hwcard{
    position: absolute;
    left: 0px;
    margin-top: 100px;
}
.hwForm{
    position: absolute;
    height: 600px;
    width: 800px;
}
</style>
