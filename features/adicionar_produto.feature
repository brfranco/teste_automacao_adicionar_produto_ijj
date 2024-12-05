Feature: Adicionar Produto

  Scenario: Adicionar um novo produto
    Given que estou na página de login
    When eu insiro credenciais válidas
    And eu clico no botão de login
    Then eu devo ser redirecionado para o painel
    And eu clico no botão "+ Adicionar"
    And eu preencho o campo "Nome do Produto" com "Camiseta"
    And eu preencho o campo "Descrição do Produto" com "Camiseta de algodão"
    And eu seleciono a categoria "ROUPAS"
    And eu preencho o campo "Preço" com "29.99"
    And eu adiciono a imagem "camiseta.jpg"
    And eu preencho o campo "Frete" com "5.00"
    And eu clico no botão "Salvar"
    Then eu devo ver uma mensagem de sucesso