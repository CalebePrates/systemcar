$(document).ready(function(){
    mascaras();
})

function mascaras() {
    $('.data_mask').keypress(function(e) {
        if(e.keyCode < 47 || e.keyCode > 57) {
            e.preventDefault();
        }
        var len = this.value.length;

        // If we're at a particular place, let the user type the slash
        // i.e., 12/12/1212
        if(len !== 1 || len !== 3) {
            if(e.keyCode == 47) {
                e.preventDefault();
            }
        }
        // If they don't add the slash, do it for them...
        if(len === 2) {
            this.value += '/';
        }
        // If they don't add the slash, do it for them...
        if(len === 5) {
            this.value += '/';
        }
    });

    $('.money_mask').mask("#,##0.00", {reverse: true});

    $('.cep_mask').mask('99999-999');

    $(".telefone_mask").mask("(99) 9999?9-9999");
    $(".telefone_mask").on("blur", function() {
        var last = $(this).val().substr( $(this).val().indexOf("-") + 1 );

        if( last.length == 3 ) {
            var move = $(this).val().substr( $(this).val().indexOf("-") - 1, 1 );
            var lastfour = move + last;
            var first = $(this).val().substr( 0, 9 );

            $(this).val( first + '-' + lastfour );
        }
    });

    $('.phone').text(function(i, text) {
        return text.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
    });

    $(".only_numbers").keypress(function (e) {
        //if the letter is not digit then display error and don't type anything
        if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           //display error message
           $("#errmsg").html("Digits Only").show().fadeOut("slow");
                return false;
       }
    });
};