<template>
    <div>
        <Carousel
            :autoplay="true"
            :autoplay-speed="setting.autoplaySpeed"
            :dots="setting.dots"
            :trigger="setting.trigger"
            :arrow="setting.arrow"
            class="carousel">
            <Carousel-item>
                <div class="demo-carousel">1</div>
            </Carousel-item>
            <Carousel-item>
                <div class="demo-carousel">2</div>
            </Carousel-item>
            <Carousel-item>
                <div class="demo-carousel">3</div>
            </Carousel-item>
            <Carousel-item>
                <div class="demo-carousel">4</div>
            </Carousel-item>
        </Carousel>
        <!--CSS两列布局，右侧固定，左侧自适应宽度 <br />-->
        <!--<div style="width:90%; margin:0 auto; overflow:auto; _display:inline-block;"> 
            <div style="width:200px; float:right; background:#090">这是右侧的内容</div> 
            <div style=" margin-right:210px; background:#F33">这是左侧的内容，自适应宽度</div> 
        </div> -->
        
        
        <!--CSS两列布局，左侧固定，右侧自适应宽度 <br />-->
        <!--<div style="width:90%; margin:0 auto; overflow:auto; _display:inline-block;"> 
            <div style="width:150px; float:left; background:#6F0">这是左侧的内容 固定宽度</div> 
            <div style=" margin-left:160px; background:#FC0">中间内容，自适应宽度</div> 
        </div> -->
        
        <!--CSS三列布局，左右宽度固定，中间自适应宽度 <br />-->
        <!--<div style="width:90%; margin:0 auto; overflow:auto; _display:inline-block;"> 
            <div style="width:200px; float:right; background:#393"> 这是右侧的内容 固定宽度</div> 
            <div style="width:150px; float:left; background:#F60 ">这是左侧的内容 固定宽度</div> 
            <div style=" margin-left:160px;margin-right:210px; background:#6C3;">中间内容，自适应宽度</div> 
        </div>-->
    </div>
</template>
<script>
    export default {
        data () {
            return {
                setting: {
                    autoplay: false,
                    autoplaySpeed: 2000,
                    dots: 'inside',
                    trigger: 'click',
                    arrow: 'hover'
                }
            }
        },
    }
</script>
<style>
    .carousel{
        position: relative;
        top: 10px;
        height: 250px;
        background: black;
        width:65%;
         /*自适应宽度*/
        margin:0 auto;
        overflow:auto;
        _display:inline-block;
    }
</style>