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

    $(".telefone_mask").mask("(00) 0000-00009");
    jQuery(".telefone_mask").mask("(99) 9999-9999?9").focusout(function (event) {  
        var target, phone, element;  
        target = (event.currentTarget) ? event.currentTarget : event.srcElement;  
        phone = target.value.replace(/\D/g, '');
        element = $(target);  
        element.unmask();  
        if(phone.length > 10) {  
            element.mask("(99) 99999-999?9");  
        } else {  
            element.mask("(99) 9999-9999?9");  
        }  
    });
};