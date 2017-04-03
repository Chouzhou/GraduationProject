<template>
    <Row class="card">
        <i-col span="6" @click.native="showCourse">
            <Card>
                <p slot="title">课程名</p>
                <p>课程简介</p>
            </Card>
        </i-col>
    </Row>
</template>
<script>
    export default {
        methods: {
            showCourse() {
                alert('成功');
            }
        }
        
    }
</script>
<style>
.card{
    left: 400px;
    top: 30px;
}
</style>