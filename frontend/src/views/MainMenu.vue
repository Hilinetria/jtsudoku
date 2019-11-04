<template>
  <section class="section">
    <div class="container">
        <div class="columns is-mobile">
            <div class="menu column is-4 is-offset-4">
                <p class="title">Sudoku</p>
                <p class="subtitle"></p>
                <b-menu>
                    <b-menu-list>
                        <router-link to="/single"><b-menu-item label="Одиночная игра"></b-menu-item></router-link>
                    </b-menu-list>
                </b-menu>
            </div>
        </div>
    </div>
  </section>
    
</template>

<script>
    export default {
        name: 'menu',
        data() {
            return {
                isActive: true
            }
        }
    }
</script>

<style>
    .menu {
        background-color: #00d1b1;
        border-radius: 5px;
    }
    .menu .title {
        color: #fff;
    }
    .menu-list a {
        color: #fff!important;
    }
    .menu-list:hover a {
        color: #000!important;
    }    
</style>
