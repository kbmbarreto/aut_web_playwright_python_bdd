from behave import given, when, then


@when('o usuário clica no botão "Quero me cadastrar"')
def step_clicar_quero_me_cadastrar(context):
    context.landing_page.click_quero_me_cadastrar_button()


@then("o título da página de cadastro deve estar visível")
def step_verificar_titulo_cadastro_visivel(context):
    assert context.cadastro_page.home_title_is_visible()
