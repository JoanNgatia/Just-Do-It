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

}

$(document).ready(main);
