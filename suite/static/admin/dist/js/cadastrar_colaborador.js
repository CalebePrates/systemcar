$(document).ready(function(){
    $('.btn-salvar').on("click", function(){
        validarCamposcolaborador();
    })
})

function validarCamposcolaborador(){
    $('.btn-salvar').prop('disabled', true);

    $('[name=nome_colaborador]').css("border-color", "#ced4da");
    $('#spanNome_colaborador').hide();
    $('[name=usuario_colaborador]').css("border-color", "#ced4da");
    $('#spanUsuario_colaborador').hide();
    $('[name=senha_colaborador]').css("border-color", "#ced4da");
    $('#spanSenha_colaborador').hide();
    $('[name=confirm_colaborador]').css("border-color", "#ced4da");
    $('#spanConfirm_colaborador').hide();
    $('[name=email_colaborador]').css("border-color", "#ced4da");
    $('#spanEmail_colaborador').hide();
    $('[name=telefone_colaborador]').css("border-color", "#ced4da");
    $('#spanTelefone_colaborador').hide();

    var idColaborador = $('[name=idColaborador]').val()
    var usuario = $('[name=usuario_colaborador]').val();
    var senha = $('[name=senha_colaborador]').val();
    var confirmSenha = $('[name=confirm_colaborador]').val();
    var nome = $('[name=nome_colaborador]').val();
    var email = $('[name=email_colaborador]').val();
    var telefone = $('[name=telefone_colaborador]').val();
    var tipocolaborador = $('[name=tipoColaborador_colaborador]').val();
    var situacaoEmpresa = $('[name=situacaoEmpresa_colaborador]').val();

    var formValido = true;

    if (nome.length < 3){
        formValido = false;
        $('[name=nome_colaborador]').css("border-color", "red");
        $('#spanNome_colaborador').show();
    }
    if (usuario.length < 3){
        formValido = false;
        $('[name=usuario_colaborador]').css("border-color", "red");
        $('#spanUsuario_colaborador').show();
    }
    if (validaEmail(email) == false){
        formValido = false;
        $('[name=email_colaborador]').css("border-color", "red");
        $('#spanEmail_colaborador').show();
    }
    if (telefone.length < 14 && telefone.length > 0){
        formValido = false;
        $('[name=telefone_colaborador]').css("border-color", "red");
        $('#spanTelefone_colaborador').show();
    }
    // se não for edição de colaborador pode verificar senha
    if ($('[name=idColaborador]').length == 0){
        if (senha == "" || senha.length < 3){
            formValido = false;
            $('[name=senha_colaborador]').css("border-color", "red");
            $('#spanSenha_colaborador').show();
        }
        if (confirmSenha == "" || senha != confirmSenha || confirmSenha.length < 3){
            formValido = false;
            $('[name=confirm_colaborador]').css("border-color", "red");
            $('#spanConfirm_colaborador').show();
        }
    } else{
        if (senha.length > 0 && senha.length < 3){
            formValido = false;
            $('[name=senha_colaborador]').css("border-color", "red");
            $('#spanSenha_colaborador').show();
        }
        if ( senha != confirmSenha || (confirmSenha.length > 0 && confirmSenha.length < 3)){
            formValido = false;
            $('[name=confirm_colaborador]').css("border-color", "red");
            $('#spanConfirm_colaborador').show();
        }
    }
    if (formValido){
        jsonData = {
            "idColaborador": idColaborador,
            "nomeColaborador": nome,
            "usuarioColaborador": usuario,
            "tipoColaborador": tipocolaborador,
            "situacaoColaborador": situacaoEmpresa,
            "senhaColaborador": senha,
            "emailColaborador": email,
            "telefoneColaborador": telefone.replace('(','').replace(')','').replace('-', '').replace(' ', '')
        }
        cadastrarColaboradorRequest(jsonData);
    } else{
        $('.btn-salvar').prop('disabled', false);
    }
}

function cadastrarColaboradorRequest(jsonData){
    $.ajax({
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        method: "POST",
        url: "/rest/cadastrar_colaborador_rest/",
        data: jsonData
    }).done(function(response) {
        $(location).attr('pathname', '/admin/listar_colaboradores/1')
    }).fail(function(response) {
        $(location).attr('pathname', '/admin/listar_colaboradores/2')
    })
}