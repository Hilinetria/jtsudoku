<template>
  <section class="section">
    <div class="container">
        <div class="columns is-mobile">
            <div class="menu column is-4 is-offset-4">
                <Field v-bind:generated="generated"></Field>
                <router-link to="/"><b-button label="Назад в меню"></b-button></router-link>
            </div>
        </div>
    </div>
  </section>
    
</template>

<script>
    import axios from 'axios'
    
    import {API_DOMAIN} from '../const'
    import Field from '../components/Field'

    export default {
        name: 'single',
        components: {
            Field,
        },        
        data () {
            return {
                generated: null
            }
        },        
        beforeRouteEnter(to, from, next) {
            axios.get(API_DOMAIN).then((response) => {
                next(vm => (vm.generated = response.data.generated))
            });
        },
    }
</script>

<style scoped>
    .menu {
        background-color: #00d1b1;
        border-radius: 5px;
    }
    .menu a {
        color: #fff;
    }
</style>
