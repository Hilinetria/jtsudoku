<template>
  <table class="field">
      <tr v-for="row in generated" v-bind:key="row">
        <td class="cell" v-for="column in row" v-bind:key="column">
          {{ column }}
        </td>
      </tr>
  </table>
</template>

<script>
export default {
  name: 'Field',
  props: ['generated'],
}
</script>

<style scoped>
  .field {
    background-color: #fff;
    border: 1px solid #ededed;
    margin: 0 auto;
  }
  .cell {
    padding: 2px 9px;
    border: 2px solid #ededed;
  }
</style>
