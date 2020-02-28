$(document).ready(function(){
    $('.btn-salvar').on("click", function(){
        validarCamposcolaborador();
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

function validarCPF(cpf) {	
	cpf = cpf.replace(/[^\d]+/g,'');	
	if(cpf == ''){
        return true;
    }
	// Elimina CPFs invalidos conhecidos	
	if (cpf.length != 11 || 
		cpf == "00000000000" || 
		cpf == "11111111111" || 
		cpf == "22222222222" || 
		cpf == "33333333333" || 
		cpf == "44444444444" || 
		cpf == "55555555555" || 
		cpf == "66666666666" || 
		cpf == "77777777777" || 
		cpf == "88888888888" || 
		cpf == "99999999999")
			return false;		
	// Valida 1o digito	
	add = 0;	
	for (i=0; i < 9; i ++)		
		add += parseInt(cpf.charAt(i)) * (10 - i);	
		rev = 11 - (add % 11);	
		if (rev == 10 || rev == 11)		
			rev = 0;	
		if (rev != parseInt(cpf.charAt(9)))		
			return false;		
	// Valida 2o digito	
	add = 0;	
	for (i = 0; i < 10; i ++)		
		add += parseInt(cpf.charAt(i)) * (11 - i);	
	rev = 11 - (add % 11);	
	if (rev == 10 || rev == 11)	
		rev = 0;	
	if (rev != parseInt(cpf.charAt(10)))
		return false;		
	return true;   
}

function validarCamposcolaborador(){
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
    $('[name=cpf_colaborador]').css("border-color", "#ced4da");
    $('#spanCpf_colaborador').hide();

    var nome = $('[name=nome_colaborador]').val();
    var usuario = $('[name=usuario_colaborador]').val();
    var tipocolaborador = $('[name=tipoColaborador_colaborador]').val();
    var situacaoEmpresa = $('[name=situacaoEmpresa_colaborador]').val();
    var senha = $('[name=senha_colaborador]').val();
    var confirmSenha = $('[name=confirm_colaborador]').val();
    var email = $('[name=email_colaborador]').val();
    var cpf = $('[name=cpf_colaborador]').val();
    var dataNascimento = $('[name=data_colaborador]').val();

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
    if (validaEmail(email) == false){
        formValido = false;
        $('[name=email_colaborador]').css("border-color", "red");
        $('#spanEmail_colaborador').show();
    }
    if (validarCPF(cpf) == false){
        formValido = false;
        $('[name=cpf_colaborador]').css("border-color", "red");
        $('#spanCpf_colaborador').show();
    }
    if (dataNascimento.length < 9 && dataNascimento.length > 0){
        formValido = false;
        $('[name=data_colaborador]').css("border-color", "red");
        $('#spanData_colaborador').show();
    }

    jsonData = {
        "nomecolaborador": nome,
        "usuariocolaborador": usuario,
        "tipocolaborador": tipocolaborador,
        "situacaoEmpresa": situacaoEmpresa,
        "senhacolaborador": senha,
        "emailcolaborador": email,
        "cpfcolaborador": cpf,
        "dataNasccolaborador": dataNascimento
    }

    if (formValido){
        cadastrarcolaborador(jsonData);
    }
}

function cadastrarcolaborador(jsonData){
    $.ajax({
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        method: "POST",
        url: "/rest/cadastrar_colaborador_rest/",
        data: jsonData
    }).done(function(response) {
        console.log(response);
    });
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}