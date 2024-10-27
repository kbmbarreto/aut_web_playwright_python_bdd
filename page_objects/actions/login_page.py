from playwright.sync_api import Page
from page_objects.elements.login_locators import LoginLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def home_title_is_visible(self) -> bool:
        return self.page.is_visible(f"text={LoginLocators.TXT_TITLE}")

    def inp_cpf_is_visible(self) -> bool:
        return self.page.is_visible(LoginLocators.INP_CPF)

    def inp_cpf_fill(self, text: str) -> None:
        return self.page.fill(LoginLocators.INP_CPF, text)

    def inp_senha_is_visible(self) -> bool:
        return self.page.is_visible(LoginLocators.INP_SENHA)

    def inp_senha_fill(self, text: str) -> None:
        return self.page.fill(LoginLocators.INP_SENHA, text)

    def btn_entrar_is_visible(self) -> bool:
        return self.page.is_visible(LoginLocators.BTN_ENTRAR)

    def txt_verifique_seus_dados_is_visible(self) -> bool:
        return self.page.is_visible(LoginLocators.TXT_VERIFIQUE_SEUS_DADOS)

    def click_entrar_button(self):
        self.page.click(LoginLocators.BTN_ENTRAR)
