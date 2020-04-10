import Vue from 'vue'
import Vuex from 'vuex'
import * as firebase from 'firebase'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user:{
            id:'',
        }
    },
    mutations: {
        setUser(state,payload){
            state.user = payload
        }
    },
    actions: {
        register({commit},payload){
            firebase.auth().createUserWithEmailAndPassword(payload.email,payload.password).then(
                user => {
                    const newUser = {
                        id:user.uid,
                    }
                    commit('setUser',newUser)
                }
            )
                .catch(
                    error => {
                        alert(error)
                    }
                )
        }
    },
    modules: {

    }
})
