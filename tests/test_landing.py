import allure
import pytest
from page_objects.actions.landing_page import LandingPage


@pytest.fixture
def landing_page(page):
    return LandingPage(page)


@allure.feature("Landing Page")
@allure.story("Exibição de Componentes")
def test_todos_os_componentes_devem_ser_exibidos(landing_page):
    landing_page.navigate_to_landingpage()
    assert landing_page.home_title_is_visible()
    assert landing_page.btn_exames_is_visible()
    assert landing_page.btn_pacientes_is_visible()
    assert landing_page.btn_faq_is_visible()
    assert landing_page.btn_entrar_is_visible()


@allure.feature("Landing Page")
@allure.story("Acesso à Página de Exames")
def test_deve_acessar_o_nav_exames_com_sucesso(landing_page):
    landing_page.navigate_to_landingpage()
    landing_page.click_exames_link()
    assert landing_page.page.url == "https://navpro.dasa.com.br/exames"
