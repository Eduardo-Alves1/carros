
  document.getElementById('resetBtn').addEventListener('click', function() {
    // Limpa o campo de busca
    document.querySelector('input[name="search"]').value = '';
    
    // Opcionalmente, submete o formulário para recarregar a página sem o filtro
    document.querySelector('form').submit();
  });
