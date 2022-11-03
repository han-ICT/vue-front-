
<template>
  <v-app id="inspire">
    <v-app-bar
      app
      clipped-right
      flat
      height="72"
      color = "#1c2331"
    >
      <v-spacer></v-spacer>
    <h3 class="title">[22_HP016] 가시광통신 기술과 GPS 기술을 활용한 실내외 구분없이 작업자의 실시간 위치 추적이 가능한 하이브리드 안전 헬멧</h3>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      app
      width="300"
      color = "#45526e"
    >

      <v-navigation-drawer
        v-model="drawer"
        absolute
        color="#2e3951"
        mini-variant
      >

        <v-avatar
          class="d-block text-center mx-auto mt-4"     
          color="grey darken-1"
          size="36"
        ></v-avatar>

        <v-divider class="mx-3 my-5"></v-divider>


        <v-avatar
          v-for="n in 6"
          :key="n"
          class="d-block text-center mx-auto mb-9"
          color="grey lighten-1"
          size="28"
        ></v-avatar>
      </v-navigation-drawer>

      <v-sheet
        color="#45526e"
        height="128"
        width="100%"
      ></v-sheet>

     <v-list
        class="pl-16"
        shaped
      >
        <v-list-item-content>
          <v-list-item-title class="message1"> 공지 </v-list-item-title>
        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title class="message1"> 사원 관리 </v-list-item-title>
        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title class="message1"> QnA 게시판 </v-list-item-title>
        </v-list-item-content>       

        <v-list-item-content>
          <v-list-item-title class="message1"> 메신저 </v-list-item-title>
        </v-list-item-content>   

        <v-list-item-content>
          <v-list-item-title class="message1"> 서버 부하 실시간 현황 </v-list-item-title>
        </v-list-item-content>

      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer
      app
      clipped
      right
      color="#45526e"
    >
      <v-list
        class="pl-6"
        shaped
      >
        <v-list-item-content>
          <v-list-item-title class="message1"> 사내 메신저 ( 활동 중 ) </v-list-item-title>
        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title > 이가람 </v-list-item-title>
          <v-list-item-title> garam1019@gmail.com </v-list-item-title>
          <v-list-item-title> 방금 </v-list-item-title>
        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title> 정우인  </v-list-item-title>
          <v-list-item-title> inside01@naver.com </v-list-item-title>
          <v-list-item-title> 3분전 </v-list-item-title>
        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title> 김강산 </v-list-item-title>
          <v-list-item-title> mountainwater@daum.net </v-list-item-title>
          <v-list-item-title> 3분전 </v-list-item-title>
        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title> 최보메 </v-list-item-title>
          <v-list-item-title> happybomr@daum.net </v-list-item-title>
          <v-list-item-title> 7분전 </v-list-item-title>

        </v-list-item-content>

        <v-list-item-content>
          <v-list-item-title> 이하이 </v-list-item-title>
          <v-list-item-title> hihihi1234@gmail.com </v-list-item-title>
          <v-list-item-title> 13분전 </v-list-item-title>
        </v-list-item-content>        
      </v-list>
    </v-navigation-drawer>

    <v-main 
    style="background: #7283a7">

    <main_text v-bind:propsdata="employeeList"></main_text>

    <v-flex class="userList" column>
      <v-card max-width="600" tile>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title> Title </v-list-item-title>
            <v-list-item-subtitle> content </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card>
    </v-flex>

    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
import Main_Text from "./components/HelloWorld.vue";
let url = "http://k8s-default-backendi-6566bc7d31-1619657679.ap-northeast-2.elb.amazonaws.com/location/";
window.setTimeout('window.location.reload()',5000);

export default{
  data: () => {
    return{
      employeeList: []
    };
  },
  components: {
    "main_text": Main_Text,
  },
  mounted(){
    axios({
      methods: "GET",
      url: url
  })
  .then(response =>{
    this.employeeList = response.data;
    console.log(response)
    console.log(response.data)
  })
  .catch(response =>{
    console.log("Failed", response);
  });
},
methods:{ //CRUD logic
  getUserList: function(){},
  updateUserList: function(){},
  deleteUserList: function(){}
}
};
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
.title {
    color: white;
    text-align: right;
    padding: 10px;
}
.message1 {
  font-size : 25px;
}
</style>