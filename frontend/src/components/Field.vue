<template>
    <table>
        <tr v-for="(row, n) in field" v-bind:key="row">
            <td v-for="(column, m) in row" v-bind:key="column">
                <input 
                    type="number" 
                    min="1" 
                    max="10" 
                    v-bind:class="{'cell':true, 'v-thrid':([2, 5].indexOf(n) > -1), 'h-thrid':([2, 5].indexOf(m) > -1)}"
                    :value="column ? column : ''" 
                />
            </td>
        </tr>
    </table>
</template>

<script>
    export default {
        name: 'Field',
        props: ['field'],
    }
</script>

<style scoped>
    table {
        background-color: #fff;
        border: none;
        margin: 0 auto;
    }

    .game-field {
        margin: 0 auto;
    }
    
    .cell {
        width: 35px;
        height: 30px;
        text-align: center;
        border: 1px dashed #ededed;
    }

    .v-thrid {
        border-bottom: 1px dashed #000;
    }

    .h-thrid {
        border-right: 1px dashed #000;
    }

    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
        -webkit-appearance: none; 
        margin: 0; 
    }
</style>
