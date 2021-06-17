const vm = new Vue({
    el: '#app',
    data: {
        results: {},
    },
    methods: {
        leaderboard: function () {
            axios({
                url: "",
                method: "GET",
                
                // looking for a reliable, free sports API
                
            }).then(response => {
                this.results = response.data
                console.log(results)
            })
        }
    }
})