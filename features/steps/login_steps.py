from behave import given, when, then
from playwright.sync_api import expect


@when('o usuário clica no botão "Entrar"')
def step_clicar_entrar_button(context):
    context.landing_page.click_entrar_button()


@then('a URL deve ser "https://navpro.dasa.com.br/auth#login"')
def step_verificar_url_login(context):
    expect(context.page).to_have_url("https://navpro.dasa.com.br/auth#login")


@when('o usuário preenche o campo CPF com "{cpf}"')
def step_preencher_cpf(context, cpf):
    context.login_page.inp_cpf_fill(cpf)


@when('o usuário preenche o campo senha com "{senha}"')
def step_preencher_senha(context, senha):
    context.login_page.inp_senha_fill(senha)


@when("o usuário clica no botão de login")
def step_clicar_entrar_login(context):
    context.login_page.click_entrar_button()


@then("a mensagem de verificação de dados deve estar visível")
def step_verificar_mensagem_erro(context):
    assert context.login_page.txt_verifique_seus_dados_is_visible()
