<template>
  <v-app>
    <v-toolbar class="blue lighten-4">
      <v-app-bar-nav-icon @click="sideNav = !sideNav"></v-app-bar-nav-icon>
      <v-toolbar-title>Celebrities Recognition</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn class="blue lighten-4">
          <v-icon left class="mdi mdi-login"></v-icon>
          Login
        </v-btn>
        <v-btn raised class="blue lighten-4">
          <v-icon left class="mdi mdi-account-plus"></v-icon>
          Sign Up
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-navigation-drawer v-model="sideNav">
    </v-navigation-drawer>
<!--      <swiper ref="mySwiper" :options="swiperOptions">-->
<!--        <swiper-slide>Slide 1</swiper-slide>-->
<!--        <swiper-slide>Slide 2</swiper-slide>-->
<!--        <swiper-slide>Slide 3</swiper-slide>-->
<!--        <swiper-slide>Slide 4</swiper-slide>-->
<!--        <swiper-slide>Slide 5</swiper-slide>-->

<!--        <div class="swiper-pagination"  slot="pagination"></div>-->
<!--        <div class="swiper-button-prev" slot="button-prev"></div>-->
<!--        <div class="swiper-button-next" slot="button-next"></div>-->
<!--        <div class="swiper-scrollbar"   slot="scrollbar"></div>-->
<!--      </swiper>-->

    <main>
<!--            <swiper ref="mySwiper" :options="swiperOptions">-->
<!--              <swiper-slide>Slide 1</swiper-slide>-->
<!--              <swiper-slide>Slide 2</swiper-slide>-->
<!--              <swiper-slide>Slide 3</swiper-slide>-->
<!--              <swiper-slide>Slide 4</swiper-slide>-->
<!--              <swiper-slide>Slide 5</swiper-slide>-->

<!--              <div class="swiper-pagination"  slot="pagination"></div>-->
<!--              <div class="swiper-button-prev" slot="button-prev"></div>-->
<!--              <div class="swiper-button-next" slot="button-next"></div>-->
<!--              <div class="swiper-scrollbar"   slot="scrollbar"></div>-->
<!--            </swiper>-->
      <swiper-slide>I am Slide 1</swiper-slide>
    </main>
  </v-app>
</template>

<script>
  import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
export default {
  name: 'App',

  components: {
    // eslint-disable-next-line vue/no-unused-components
    Swiper,
    // eslint-disable-next-line vue/no-unused-components
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  // computed:{
  //   swiper(){
  //     return this.$refs.mySwiper.swiper
  //   }
  // },
  // mounted() {
  //   console.log('mounted');
  // },

  data(){
    return{
      // swiperOption:{
      //   notNextTick:true,
      //   autoplay:3000,
      //   effect:"coverflow",
      //   grabCursor:true,
      //   setWrapperSize:true,
      //   pagination:'.swiper-pagination',
      //   paginationClickable:true,
      //   prevButton:".swiper-button-prev",
      //   nextButton:".swiper-button-next",
      //   observeParents:true,
      // },
      sideNav:false
    }
  }
  // data: () => ({
  //   sideNav:false
  // }),
};
</script>
