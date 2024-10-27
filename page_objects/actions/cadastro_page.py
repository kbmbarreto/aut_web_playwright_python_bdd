from playwright.sync_api import Page
from page_objects.elements.cadastro_locators import CadastroLocators


class CadastroPage:
    def __init__(self, page: Page):
        self.page = page

    def home_title_is_visible(self) -> bool:
        return self.page.is_visible(CadastroLocators.TXT_TITLE)

    def click_fechar_button(self):
        self.page.click(CadastroLocators.BTN_PROXIMO)
