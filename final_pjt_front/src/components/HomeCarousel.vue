<template>
  <div></div>
  <!-- <div>
    <splide :options="options">
      <splide-slide>
        <img src="image1.jpg" />
      </splide-slide>
      <splide-slide>
        <img src="image2.jpg" />
      </splide-slide>
      <splide-slide>
        <img src="image3.jpg" />
      </splide-slide>
    </splide>
  </div> -->
</template>

<script>
// import { Splide, SplideSlide } from "@splidejs/vue-splide";
// import "@splidejs/splide/dist/css/themes/splide-default.min.css";

export default {
  name: "HomeCarousel",
  components: {},
  data: function () {
    return {
      options: {
        rewind: true,
        width: 800,
        gap: "1rem",
      },
    };
  },
};
</script>

<style>
</style>