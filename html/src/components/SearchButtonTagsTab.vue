<template>
  <v-container>
    <v-text-field label="Search Tags"></v-text-field>
    <v-row>
      <v-col cols="12" md="6">
        <v-text-field density="compact" label="Page Size"></v-text-field
      ></v-col>
      <v-col cols="12" md="6">
        <v-text-field density="compact" label="Current Pages"></v-text-field
      ></v-col>
    </v-row>
    <v-row justify="space-evenly">
      <v-btn type="submit">Save</v-btn
      ><v-btn type="submit" @click="console.log('Hiiiii')">Run</v-btn>
    </v-row>
  </v-container>
</template>
