$(function() {

    $('#registration-link').on ("click", function(e){
        e.preventDefault();
        $('.registrationform').show();
        $('.loginform').hide();
    });

    $('#login-link').on ("click", function(e){
        e.preventDefault();
        $('.registrationform').hide();
        $('.loginform').show();
    });
});
