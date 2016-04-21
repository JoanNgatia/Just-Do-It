// Using jQuery
$.ajax({
    type: "GET",
    headers: {"Access-Control-Allow-Origin": "*"},
    url: "http://localhost:8000/bucketlists/"
}).done(function (data) {
    console.log(data);
});

var main = function() {
    $('#all_bucketlists').click(function(){
        $('#newbucketModal').modal('show');
    });

    $('#deleteBucket').click(function(){
        $('#deleteBucketlistModal').modal('show');
    });

    $('[data-toggle="tooltip"]').tooltip({animation: true, delay: {show: 300, hide: 300}});

    $(".flash-message").fadeOut(4000);
}

$(document).ready(main);


$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});