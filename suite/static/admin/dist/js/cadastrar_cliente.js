$(document).ready(function(){
    $('.btn-salvar').on("click", function(){
        validarCamposCliente();
    })
})

function validaEmail(email) {
    if (email == ""){
        return true;
    } else{
        var regex = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
        return regex.test(email);
    }
}

function validarCamposCliente(){
    $('[name=nome_cliente]').css("border-color", "#ced4da");
    $('#spanNome_cliente').hide();
    $('[name=usuario_cliente]').css("border-color", "#ced4da");
    $('#spanUsuario_cliente').hide();
    $('[name=senha_cliente]').css("border-color", "#ced4da");
    $('#spanSenha_cliente').hide();

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
        $('#spanNome_cliente').show();
    }
    if (usuario.length < 3 || usuario == ""){
        formValido = false;
        $('[name=usuario_cliente]').css("border-color", "red");
        $('#spanUsuario_cliente').show();
    }
    if (senha == "" || senha.length < 3){
        formValido = false;
        $('[name=senha_cliente]').css("border-color", "red");
        $('#spanSenha_cliente').show();
    }
    if (confirmSenha == "" || senha != confirmSenha || confirmSenha.length < 3){
        formValido = false;
        $('[name=confirm_cliente]').css("border-color", "red");
        $('#spanConfirm_cliente').show();
    }
    if (validaEmail(email) == false){
        formValido = false;
        $('[name=email_cliente]').css("border-color", "red");
        $('#spanEmail_cliente').show();
    }

    jsonData = {
        "nomeCliente": nome,
        "usuarioCliente": usuario,
        "tipoCliente": tipoCliente,
        "senhaCliente": senha,
        "emailCliente": email,
        "cpfCliente": cpf,
        "dataNascCliente": dataNascimento
    }

    if (formValido){
        cadastrarCliente(jsonData);
    }
}

function cadastrarCliente(jsonData){

}