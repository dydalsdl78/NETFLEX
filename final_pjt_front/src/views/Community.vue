<template>
  <div id="Community">
    <h2>Community</h2>
    
    <Username />
    <ReviewList />
  </div>
</template>

<script>
import Username from '@/views/Username'
import ReviewList from '@/components/ReviewList'

export default {
  name:'Community',
  components: {Username, ReviewList},
};
</script>

<style>
#Community{
  background-color: black;
}
</style>