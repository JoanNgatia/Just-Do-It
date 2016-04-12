var main = function() {

    $('#login').click(function(){
        $('#loginModal').modal('show');
    });

    $('#register').click(function(){
        $('#registerModal').modal('show');
    });

    $('#all_bucketlists').click(function(){
        $('#newbucketModal').modal('show');
    });

    $('[data-toggle="tooltip"]').tooltip({animation: true, delay: {show: 300, hide: 300}});
}

$(document).ready(main);