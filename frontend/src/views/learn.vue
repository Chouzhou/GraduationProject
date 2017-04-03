<template>
    <div class="learn">
        <div class="learnTag">
                <Tag type="dot" color="blue" @click.native="allHomeWork()">所有课程</Tag>
                <Tag type="dot" color="green" @click.native="doHomeWork()">已选课程</Tag>
                <Tag type="dot" color="red" @click.native="notDoHomeWork()">已完成课程</Tag>
        </div>
        <Row class="card">
            <i-col span="6" @click.native="showCourse">
                <Card>
                    <p slot="title">课程名</p>
                    <p>课程简介</p>
                    <p>选择</p>
                </Card>
            </i-col>
        </Row>
    </div>
</template>
<script>
    export default {
        methods: {
            showCourse() {
                this.$router.push('/student/detailCouser')
            }
        }
        
    }
</script>
<style>
.learn{
    position: relative;
}
.card{
    position: relative;
    left: 400px;
    top: 30px;
}
.learnTag{
    position: relative;
    left: 400px;
    top: 30px; 
}
</style>