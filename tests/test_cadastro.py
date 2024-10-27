import allure
import pytest

from page_objects.actions.cadastro_page import CadastroPage
from page_objects.actions.landing_page import LandingPage


@pytest.fixture
def landing_page(page):
    return LandingPage(page)


@pytest.fixture
def cadastro_page(page):
    return CadastroPage(page)


@allure.feature("Cadastro Page")
@allure.story("Exibição de Componentes")
def test_todos_os_componentes_devem_ser_exibidos(landing_page, cadastro_page):
    landing_page.navigate_to_landingpage()
    assert landing_page.home_title_is_visible()
    landing_page.click_quero_me_cadastrar_button()
    assert cadastro_page.home_title_is_visible()
