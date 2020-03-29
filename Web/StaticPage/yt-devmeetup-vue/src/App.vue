<template>
  <v-app>
    <v-toolbar>
      <v-app-bar-nav-icon @click="sideNav = !sideNav"></v-app-bar-nav-icon>
      <v-toolbar-title>DevMeetups</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn raised>
          <v-icon left class="mdi mdi-account-supervisor"></v-icon>
          View Meetups
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-navigation-drawer v-model="sideNav">
    </v-navigation-drawer>
  </v-app>
</template>

<script>
  import { mdiAccountSupervisor } from '@mdi/js';

export default {
  name: 'App',
  components: {
    mdiAccountSupervisor,
  },
  data: () => ({
    sideNav:true
  }),
};
</script>
