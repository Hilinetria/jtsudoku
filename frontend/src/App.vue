<template>
    <div id="app">
        <section class="section">
            <div class="container">
                <router-view/>
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        name: 'app',
    }
</script>

<style>
    html, body {
        min-height: 100%;
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        min-height: 100%;
    }
</style>
