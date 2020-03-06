$(document).ready(function(){
  var valor_retorno = $('[name=valor_retorno_cadastro]').val()

  if (valor_retorno == 1){ // Sucesso no cadastro
    $.confirm({
      theme: 'modern',
      title: 'Sucesso!',
      content: 'Novo colaborador foi cadastrado no sistema.',
      type: 'green',
      icon: 'fas fa-check-circle',
      typeAnimated: true,
      buttons: false,
    });
  } 
  else if (valor_retorno == 2){ // Erro no cadastro
    $.confirm({
      theme: 'modern',
      title: 'Erro!',
      content: 'Novo colaborador não foi cadastrado no sistema! Tente novamente mais tarde ou entre em contato com o suporte.',
      type: 'red',
      icon: 'fas fa-sad-tear',
      typeAnimated: true,
      buttons: false,
    });
  }
})