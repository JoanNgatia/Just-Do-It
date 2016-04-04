var main = function() {

    $('#login').click(function(){
        $('#loginModal').modal('show');
    });

    $('#register').click(function(){
        $('#registerModal').modal('show');
    });

}

$(document).ready(main);
