<template>
  <section class="section">
    <div class="container">
        <div class="columns is-mobile">
            <div class="field column is-4 is-offset-4">
                <p class="title">Sudoku</p>
                <ul class="menu">
                    <li>
                        <router-link to="/single">Одиночная игра</router-link>
                    </li>
                </ul>
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

<style lang="sass">
    .field
        width: 550px;
        margin: 125px auto;
        padding: 25px;
        background-color: #43B3E9;
        border-radius: 5px;

    .field .title
        color: #fff;
        font-size: 24px;
        padding: 24px 0;
        text-align: center;

    .menu
        list-style-type: none;
        padding: 0;
        margin: 0 15px;
    
    .menu li
        margin-bottom: 10px;

    .menu li:hover
        background-color: #fff;
        border-radius: 5px;
    
    .menu li a
        display: block;
        padding: 10px;
        text-decoration: none;
        color: #fff;

    .menu li:hover a
        color: #666;   
</style>
