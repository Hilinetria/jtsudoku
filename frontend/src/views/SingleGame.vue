<template>
    <section class="section">
        <div class="container">
            <div class="columns is-mobile">
                <div class="field game-field column is-4 is-offset-4">
                    <p class="title">Одиночная игра</p>

                    <!-- Отображаем индикатор загрузки -->
                    <LoadingSpin v-if="is_loading"></LoadingSpin>
                    
                    <!-- Отображаем игровое поле если все загрузилось -->
                    <div v-else>
                        <Field v-bind:field="field"></Field>
                        <router-link to="/"><b-button label="Назад в меню"></b-button></router-link>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import axios from 'axios'
    
    import {API_DOMAIN} from '../const'
    import Field from '../components/Field'
    import LoadingSpin from '../components/LoadingSpin'

    export default {
        name: 'single',
        components: {
            Field,
            LoadingSpin,
        },        
        data () {
            return {
                is_loading: true,
                field: [],
            }
        },        
        mounted() {
            axios.get(API_DOMAIN).then((response) => {
                this.is_loading = false
                this.field = response.data.generated
            });
        },
    }
</script>

<style scoped>
    .game-field {
        min-height: 350px;
    }
</style>
