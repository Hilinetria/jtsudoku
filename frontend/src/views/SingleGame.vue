<template>
    <section class="section">
        <div class="container">
            <div class="columns is-mobile">
                <div class="field game-field column is-4 is-offset-4">
                    <p class="title">Одиночная игра</p>

                    <!-- Отображаем индикатор загрузки -->
                    <loading_spin v-if="is_loading"></loading_spin>
                    
                    <!-- Отображаем игровое поле если все загрузилось -->
                    <div v-else>
                        <field v-bind:data="data"></Field>
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
    import field from '../components/Field'
    import loading_spin from '../components/LoadingSpin'

    export default {
        name: 'single',
        components: {
            field,
            loading_spin,
        },        
        data () {
            return {
                is_loading: true,
                data: [],
            }
        },        
        mounted() {
            axios.get(API_DOMAIN).then((response) => {
                this.is_loading = false
                this.data = response.data.generated
            });
        },
    }
</script>

<style scoped lang="sass">
    .game-field
        min-height: 350px;
</style>
