<template>
  <carousel
    :navigationEnabled="true"
    :perPage="1"
    :scrollPerPage="true"
    :paginationEnabled="true"
  >
    <slide>
      <img
        src="@/assets/ddd.jpg"
        alt=""
        class="test"
        style="width: 100%"
      />
      <p class="img-content">11월 4주차 인기작</p>
    </slide>
    <slide
      ><img
        src="@/assets/ccc.jpg"
        alt=""
        style="width: 100%"
      />

  </slide
    >
    <slide
      ><img
        src="@/assets/aaa.png"
        alt=""
        style="width: 100%"
      />
    </slide>
  </carousel>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";
export default {
  name: "HomeCarousel",
  components: {
    Carousel,
    Slide,
  },
  data: function () {
    return {};
  },
};
</script>

<style>
.VueCarousel .VueCarousel-navigation-button {
  color: white;
}
.test {
  z-index: 0;
}

.img-content {
  z-index: 10;
  font-size: 40px;
  top: 40%;
  left: 20%;
}
</style>