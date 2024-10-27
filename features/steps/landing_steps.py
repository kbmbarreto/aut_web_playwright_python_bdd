from behave import given, when, then
from playwright.sync_api import expect


@then("o título da página deve estar visível")
def step_verificar_titulo_visivel(context):
    assert context.landing_page.home_title_is_visible()


@then("o botão Exames deve estar visível")
def step_verificar_botao_exames_visivel(context):
    assert context.landing_page.btn_exames_is_visible()


@then("o botão Pacientes deve estar visível")
def step_verificar_botao_pacientes_visivel(context):
    assert context.landing_page.btn_pacientes_is_visible()


@then("o botão FAQ deve estar visível")
def step_verificar_botao_faq_visivel(context):
    assert context.landing_page.btn_faq_is_visible()


@then("o botão Entrar deve estar visível")
def step_verificar_botao_entrar_visivel(context):
    assert context.landing_page.btn_entrar_is_visible()


@when("o usuário clica no link de Exames")
def step_clicar_link_exames(context):
    context.landing_page.click_exames_link()


@then('a URL deve ser "https://navpro.dasa.com.br/exames"')
def step_verificar_url_exames(context):
    expect(context.page).to_have_url("https://navpro.dasa.com.br/exames")
