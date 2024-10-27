Feature: Landing Page

  Scenario: Exibição de todos os componentes
    Given que o usuário acessa a página inicial
    Then o título da página deve estar visível
    And o botão Exames deve estar visível
    And o botão Pacientes deve estar visível
    And o botão FAQ deve estar visível
    And o botão Entrar deve estar visível

  Scenario: Acessar a página de Exames
    Given que o usuário acessa a página inicial
    When o usuário clica no link de Exames
    Then a URL deve ser "https://navpro.dasa.com.br/exames"
