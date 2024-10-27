from behave import given
from page_objects.actions.landing_page import LandingPage
from page_objects.actions.cadastro_page import CadastroPage
from page_objects.actions.login_page import LoginPage


@given("que o usuário acessa a página inicial")
def step_acessar_pagina_inicial(context):
    context.landing_page = LandingPage(context.page)
    context.cadastro_page = CadastroPage(context.page)
    context.login_page = LoginPage(context.page)
    context.landing_page.navigate_to_landingpage()
