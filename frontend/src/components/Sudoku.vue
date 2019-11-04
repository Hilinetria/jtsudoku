<template>
  <div class="sudoku">
    <h1>Sudoku</h1>
    <div v-if="field !== null"><Field v-bind:generated="generated"></Field></div>
    <button v-on:click="get_field">Get field</button>
  </div>
</template>

<script>
import axios from 'axios';

import Field from './Field.vue';

export default {
  name: 'Sudoku',
  components: {
    Field,
  },
  data: function(){
    return {generated: null}
  },
  methods: {
      get_field(){
        axios
          .get('http://0.0.0.0:8081')
          .then(response => (this.generated = response.data.generated));
          // conlose.log();
      },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
