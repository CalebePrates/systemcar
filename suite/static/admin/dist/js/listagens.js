$(document).ready(function(){
  var valor_retorno = $('[name=valor_retorno_cadastro]').val()
  var valor_url = $('[name=valor_url_cadastro]').val()
  var valor_modal = $('[name=valor_modal_cadastro]').val()

  if (valor_retorno == 1){ // Sucesso no cadastro
    history.replaceState({}, null, "/admin/"+ valor_url +"/") //remove o numero da URL
    $.confirm({
      theme: 'modern',
      title: 'Sucesso!',
      content: 'Novo ' + valor_modal + ' foi cadastrado ou alterado no sistema.',
      type: 'green',
      icon: 'fas fa-check-circle',
      typeAnimated: true,
      buttons: false,
    });
  } 
  else if (valor_retorno == 2){ // Erro no cadastro
    history.replaceState({}, null, "/admin/"+ valor_url +"/") //remove o numero da URL
    $.confirm({
      theme: 'modern',
      title: 'Erro!',
      content: 'Novo ' + valor_modal + ' não foi cadastrado ou alterado no sistema! Tente novamente mais tarde ou entre em contato com o suporte.',
      type: 'red',
      icon: 'fas fa-sad-tear',
      typeAnimated: true,
      buttons: false,
    });
  }
})