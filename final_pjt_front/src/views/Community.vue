<template>
  <div id="Community">
    <h2 class="m-5">Community</h2>
    <ReviewList />
  </div>
</template>

<script>
import ReviewList from "@/components/ReviewList";

export default {
  name: "Community",
  components: { ReviewList },
};
</script>

<style>
#Community {
  background-color: black;
}
</style>