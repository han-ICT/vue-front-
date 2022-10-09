
<template>
    <div>
        <v-container fluid>
            <v-layout column>
                <v-flex xs12>
                    <p class="subject">근무자에게 메세지 보내기</p>
                </v-flex>
                <v-flex column>
                    <v-row>
                        <v-col cols="2" md="2">
                            <v-text-field v-model="employee_id" label="근무자ID" required></v-text-field>
                        </v-col>
                        <v-col cols="9" md="9">
                            <v-text-field v-model="message" label="메세지 내용" required></v-text-field>
                        </v-col>
                    </v-row>

                    <v-form ref="form" v-model="valid" lazy-validation>
                        <v-btn @click="create" style="background: green">보내기</v-btn>
                        <v-btn @click="clear" style="background: red">취소</v-btn>
                    </v-form>
                </v-flex>

                <!-- 근무자 표 !!. -->
                <!-- 근무자 표 !!. -->
                <p class="subject">근무자 현재 위치</p>
                <v-flex class="userList" column>
                    <v-card max-width="600" tile>
                        <v-list-item v-for="(data, index) in propsdata" v-bind:key="index">
                            <v-list-item-content>
                                <v-list-item-title>employee_id : {{ data.employee_id }}</v-list-item-title>
                                <v-list-item-subtitle>이름 : {{ data.name }}, 현재 위치: {{ data.location }}</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-flex>
                <!-- 수정 부분 end -->
            </v-layout>
        </v-container>
    </div>
</template>

<script>
export default {
	props:["propsdata"]
};
</script>

<style>
.subject {
    color: blue;
    font-style: oblique;
    font-size: 30px;
    padding: 30px;
    text-align: center;
}
.userList {
    font-size: 200px;
    margin: 30px 0px 30px 0px;
}
</style>