$(document).ready(function(){
    $('.btn-salvar').on("click", function(){
        validarCamposCliente();
    })
})

function validaEmail(email) {
    var regex = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return regex.test(email);
}

function validarCamposCliente(){
    $('#spanNome').hide()
    $('[name=nome]').css("border-color", "#ced4da");

    var nome = $('[name=nome]').val();
    
    var formValido = true;

    if (nome.length < 3 || nome == ""){
        formValido = false;
        $('[name=nome]').css("border-color", "red");
        $('#spanNome').show()
    }

    if (formValido){
        cadastrarCliente();
    }
}

function cadastrarCliente(){

}