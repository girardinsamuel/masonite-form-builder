
// const echo = new Echo;
// const bard = new Bard;
// const keys = new Keys;
// const hooks = new Hooks;
// const components = new Components;
const components = []
// const conditions = new FieldConditions;

export default {
    data() {
        return {
            bootingCallbacks: [],
            bootedCallbacks: [],
        }
    },

    computed: {

        $components() {
            return components;
        },

        // $request() {
        //     return this.$axios;
        // },

        // $echo() {
        //     return echo;
        // },

        // $bard() {
        //     return bard;
        // },

        // $hooks() {
        //     return hooks;
        // },

        // $conditions() {
        //     return conditions;
        // },

        // $keys() {
        //     return keys;
        // },

        // user() {
        //     return this.$config.get('user');
        // }

    },

    methods: {
        booting(callback) {
            this.bootingCallbacks.push(callback);
        },

        booted(callback) {
            this.bootedCallbacks.push(callback);
        },

        app(app) {
            this.$app = app;
        },


        start() {
            this.bootingCallbacks.forEach(callback => callback(this));
            this.bootingCallbacks = [];

            this.$app = this

            // this.$components.$root = this.$app;

            this.bootedCallbacks.forEach(callback => callback(this));
            this.bootedCallbacks = [];
        },

        component(name, component) {
            Vue.component(name, component);
        }
    }
}
