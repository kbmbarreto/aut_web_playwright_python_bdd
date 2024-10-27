import time

import allure
import pytest
from page_objects.actions.landing_page import LandingPage
from page_objects.actions.login_page import LoginPage


@pytest.fixture
def landing_page(page):
    return LandingPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@allure.feature("Login Page")
@allure.story("Acesso à Página de Login")
def test_deve_acessar_o_login_com_sucesso(landing_page):
    landing_page.navigate_to_landingpage()
    landing_page.click_entrar_button()
    assert landing_page.page.url == "https://navpro.dasa.com.br/auth#login"


@allure.feature("Login Page")
@allure.story("Login sem sucesso")
def test_deve_ter_login_recusado(landing_page, login_page):
    landing_page.navigate_to_landingpage()
    landing_page.click_entrar_button()
    assert landing_page.page.url == "https://navpro.dasa.com.br/auth#login"
    login_page.inp_cpf_fill("01520861028")
    login_page.inp_senha_fill("Teste@123")
    login_page.click_entrar_button()
    time.sleep(5)
    assert login_page.txt_verifique_seus_dados_is_visible()
    # Ou -> login_page.page.wait_for_selector(LoginLocators.TXT_VERIFIQUE_SEUS_DADOS)
