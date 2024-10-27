Feature: Login Page

  Scenario: Acessar a página de login com sucesso
    Given que o usuário acessa a página inicial
    When o usuário clica no botão "Entrar"
    Then a URL deve ser "https://navpro.dasa.com.br/auth#login"

  Scenario: Tentativa de login sem sucesso
    Given que o usuário acessa a página inicial
    When o usuário clica no botão "Entrar"
    And o usuário preenche o campo CPF com "01520861028"
    And o usuário preenche o campo senha com "Teste@123"
    And o usuário clica no botão de login
    Then a mensagem de verificação de dados deve estar visível
