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
    $('[name=nome_cliente]').css("border-color", "#ced4da");

    var nome = $('[name=nome_cliente]').val();
    var usuario = $('[name=usuario_cliente]').val();
    var tipoCliente = $('[name=tipoCliente_cliente]').val();
    var senha = $('[name=senha_cliente]').val();
    var confirmSenha = $('[name=confirm_cliente]').val();
    var email = $('[name=email_cliente]').val();
    var cpf = $('[name=cpf_cliente]').val();
    var dataNascimento = $('[name=data_cliente]').val();
    
    var formValido = true;

    if (nome.length < 3 || nome == ""){
        formValido = false;
        $('[name=nome_cliente]').css("border-color", "red");
        $('#spanNome').show()
    }

    if (formValido){
        cadastrarCliente();
    }
}

function cadastrarCliente(){

}