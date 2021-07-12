console.log("CHAL GYA")

const url = window.location.href;

$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response) {
        console.log(response)
    },
    error: function(err) {
        console.log(err)
    }
})