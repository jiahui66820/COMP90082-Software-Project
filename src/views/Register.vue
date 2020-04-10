<template>
    <div class="register">
        <RegisterPage msg="Welcome to Your Vue.js App"/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import RegisterPage from '@/components/Register.vue'

    export default {
        name: 'Register',
        components: {
            RegisterPage
        }
    }
</script>