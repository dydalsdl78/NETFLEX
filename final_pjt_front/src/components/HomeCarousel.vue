<template>
  <carousel
    :navigationEnabled="true"
    :perPage="1"
    :scrollPerPage="true"
    :paginationEnabled="true"
  >
    <slide
      ><img
        src="https://t1.daumcdn.net/cfile/tistory/99713B485DE860D201"
        alt=""
        class="test"
        style="width: 1400px"
      />
      <span class="img-content">11월 4주차 인기작</span>
    </slide>
    <slide
      ><img
        src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile29.uf.tistory.com%2Fimage%2F9940613C5A62F7001A341B"
        alt=""
        style="width: 1400px"
      />
      <span class="img-content">코로나 때문에 집에 있을 때</span>
      <span class="img-content">보기 좋은 미드!</span></slide
    >
    <slide
      ><img
        src="https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F2433A93C53C72A6C2B8C64"
        alt=""
        style="width: 1400px"
      />
      <span class="img-content">싸피릭스</span>
      <span class="img-content">최고 인기 시리즈</span></slide
    >
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