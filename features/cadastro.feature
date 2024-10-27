Feature: Cadastro Page

  Scenario: Exibição de todos os componentes na página de cadastro
    Given que o usuário acessa a página inicial
    When o usuário clica no botão "Quero me cadastrar"
    Then o título da página de cadastro deve estar visível
