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

    $("#flash-message").fadeOut(3000);
}

$(document).ready(main);

/* Toggle between adding and removing the "active" and "show" classes when the user clicks on one of the "Section" buttons. The "active" class is used to add a background color to the current button when its belonging panel is open. The "show" class is used to open the specific accordion panel */
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
    }
}
