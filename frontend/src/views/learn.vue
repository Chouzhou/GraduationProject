<template>
    <Row class="card">
        <i-col span="6">
            <Card>
                <p slot="title">标准卡片</p>
                <p>卡片内容</p>
                <p>卡片内容</p>
                <p>卡片内容</p>
            </Card>
        </i-col>
        <i-col span="6" offset="2">
            <Card>
                <p slot="title">禁用悬停阴影的卡片</p>
                <p>卡片内容</p>
                <p>卡片内容</p>
                <p>卡片内容</p>
            </Card>
        </i-col>
    </Row>
</template>
<script>
    export default {
        
    }
</script>
<style>
.card{
    left: 400px;
    top: 30px;
}
</style>