<template>
    <div class="loading-spin">
        <div class="outside-square"></div>
        <div class="inside-square"></div>
    </div>
</template>

<script>
    export default {
        name: 'loading_spin',
    }
</script>

<style scoped lang="sass">
    .loading-spin 
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        min-height: 250px;
        min-width: 100%;
        max-width: 100%;
        overflow: hidden;

    .outside-square,
    .inside-square
        position: absolute
        animation: sideBouncing .3s ease-in-out infinite

    .outside-square
        background-color: #fff
        height: 150px
        width: 150px
        animation-direction: alternate-reverse
        box-shadow: 0px 0px 12px 0px rgba(0,0,0,.3)

    .inside-square
        background-color: #4A4A4A
        height: 80px
        width: 80px
        animation-direction: alternate

    @keyframes sideBouncing
        0%
            transform: rotate(-5deg)
        100%
            transform: rotate(5deg)
</style>
