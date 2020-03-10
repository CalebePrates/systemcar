$(document).ready(function(){
    $('.btn-salvar').on("click", function(){
        validarCamposcliente();
    })
})

function validarCamposcliente(){
    $('.btn-salvar').prop('disabled', true);

    $('[name=nome_cliente]').css("border-color", "#ced4da");
    $('#spanNome_cliente').hide();
    $('[name=email_cliente]').css("border-color", "#ced4da");
    $('#spanEmail_cliente').hide();
    $('[name=telefone_cliente]').css("border-color", "#ced4da");
    $('#spanTelefone_cliente').hide();
    $('[name=cpf_cliente]').css("border-color", "#ced4da");
    $('#spanCpf_cliente').hide();
    $('[name=data_cliente]').css("border-color", "#ced4da");
    $('#spanData_cliente').hide();

    var idCliente = $('[name=idCliente]').val()
    var nome = $('[name=nome_cliente]').val();
    var email = $('[name=email_cliente]').val();
    var telefone = $('[name=telefone_cliente]').val();
    var tipocliente = $('[name=tipoCliente_cliente]').val();
    var cpf = $('[name=cpf_cliente]').val();
    var dataNascimento = $('[name=data_cliente]').val();

    var formValido = true;

    if (nome.length < 3){
        formValido = false;
        $('[name=nome_cliente]').css("border-color", "red");
        $('#spanNome_cliente').show();
    }
    if (validaEmail(email) == false){
        formValido = false;
        $('[name=email_cliente]').css("border-color", "red");
        $('#spanEmail_cliente').show();
    }
    if (telefone.length < 14 && telefone.length > 0){
        formValido = false;
        $('[name=telefone_cliente]').css("border-color", "red");
        $('#spanTelefone_cliente').show();
    }
    if (validarCPF(cpf) == false){
        formValido = false;
        $('[name=cpf_cliente]').css("border-color", "red");
        $('#spanCpf_cliente').show();
    }
    if (dataNascimento.length < 10 && dataNascimento.length < 0){
        formValido = false;
        $('[name=data_cliente]').css("border-color", "red");
        $('#spanData_cliente').show();
    }
    if (formValido){
        jsonData = {
            "idCliente": idCliente,
            "nomeCliente": nome,
            "tipoCliente": tipocliente,
            "emailCliente": email,
            "cpfCliente": cpf,
            "dataNascimentoCliente": dataNascimento,
            "telefoneCliente": telefone.replace('(','').replace(')','').replace('-', '').replace(' ', '')
        }
        cadastrarClienteRequest(jsonData);
    } else{
        $('.btn-salvar').prop('disabled', false);
    }
}

function cadastrarClienteRequest(jsonData){
    $.ajax({
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        method: "POST",
        url: "/rest/cadastrar_cliente_rest/",
        data: jsonData
    }).done(function(response) {
        $(location).attr('pathname', '/admin/listar_clientes/1')
    }).fail(function(response) {
        $(location).attr('pathname', '/admin/listar_clientes/2')
    })
}