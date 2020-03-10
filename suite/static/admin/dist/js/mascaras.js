$(document).ready(function(){
    mascaras();
})

function mascaras() {
    $('.data_mask').keypress(function(e) { // mascara para data
        if(e.keyCode < 47 || e.keyCode > 57) {
            e.preventDefault();
        }
        var len = this.value.length;
        if(len !== 1 || len !== 3) {
            if(e.keyCode == 47) {
                e.preventDefault();
            }
        }
        if(len === 2) {
            this.value += '/';
        }
        if(len === 5) {
            this.value += '/';
        }
    });

    $('.cpf_mask').mask('999.999.999-99');

    $('.money_mask').mask("#,##0.00", {reverse: true}); // mascara para dinheiro

    $('.cep_mask').mask('99999-999'); // mascara para CEP

    $(".telefone_mask").mask("(99) 9999?9-9999"); //mascara para telefone
    $(".telefone_mask").on("blur", function() {
        var last = $(this).val().substr( $(this).val().indexOf("-") + 1 );

        if( last.length == 3 ) {
            var move = $(this).val().substr( $(this).val().indexOf("-") - 1, 1 );
            var lastfour = move + last;
            var first = $(this).val().substr( 0, 9 );

            $(this).val( first + '-' + lastfour );
        }
    });

    $('.phone').text(function(i, text) { // mascara para telefone TEXT
        return text.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
    });

    $(".only_numbers").keypress(function (e) { // mascara para apenas numeros
        if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
           $("#errmsg").html("Digits Only").show().fadeOut("slow");
                return false;
       }
    });
};