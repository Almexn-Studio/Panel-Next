<script setup lang="ts">
useHead({title:"控制台首页｜FuCube"})
</script>

<template>
 
  <a-alert
      message="欢迎来到Panel Next，如遇问题请联系管理员"
      description=""
      type="info"
      show-icon
      
    />
    
 <a-carousel class="pt-4" autoplay>
    <div><h3>1</h3></div>
    <div><h3>2</h3></div>
    <div><h3>3</h3></div>
    <div><h3>4</h3></div>
  </a-carousel>

 <div class="pt-4">
  <a-card>
    <a-avatar :size="60" />
    <strong>
    {user.name}
    </strong>
     <a-divider />
     <a-statistic title="我的积分" :value="112893" style="margin-right: 50px">
      <template #suffix>
       <a-button size="small" type="primary">签到</a-button>
      </template>
     </a-statistic>
 </a-card>
 </div>

 <div class="pt-4">
  <a-card title="我的实例">
    <a-empty>
    <template #description>
      <span>
        当前暂无可用实例
      </span>
    </template>
    <a-button @click="useRouter().push('/server/create')" type="primary">立即创建</a-button>
    </a-empty>
  </a-card>
 </div>
</template>

<style scoped>
/* For demo */
:deep(.slick-slide) {
  text-align: center;
  height: 160px;
  line-height: 160px;
  background: #364d79;
  overflow: hidden;
}

:deep(.slick-slide h3) {
  color: #fff;
}
</style>
