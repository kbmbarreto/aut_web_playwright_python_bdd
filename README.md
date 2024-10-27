# aut_web_playwright_navpro

<p>Automação do portal NAV Pro, da empresa DASA, para fins acadêmicos e aprendizado do Playwright</p>

## Ferramentas utilizadas

- Python 3.12
- Playwright 1.47.0
- Pytest 8.3.3
- Pytest Html 4.1.1
- Allure Report 2.13.5

## Execução
Para executar, utilize o comando do Pytest na raiz do projeto:

<br>`pytest` -> executa todos os testes do projeto;
<br>`pytest -v` -> executa os testes exibindo mais detalhes no console;

<br>`pytest --cache-clear` -> limpa o cache do pytest.

## Execução gerando relatórios
Para executar utilizando o `pytest html`:

<br>`pytest --html=report.html` -> executa os testes e gera o relatório em html.

Para executar utilizando o `allure report`:

<br>`pytest --alluredir=allure-results` -> executa os testes e gera o relatório;
<br>`allure serve allure-results` -> gera o relatório do allure.


### O projeto ainda está em constantes melhorias, sendo atualizado a cada alteração.


## Documentação do projeto.
````
aut_web_playwright_navpro/
├── .venv/
├── page_objects/
│   ├── actions/
│   │   ├── cadastro_page.py
│   │   └── landing_page.py
│   ├── elements/
│   │   ├── cadastro_locators.py
│   │   └── landing_locators.py
├── support/
│   └── utils.py
├── tests/
│   ├── test_cadastro.py
│   └── test_landing.py
├── .gitignore
├── conftest.py
├── README.md
└── requirements.txt
````

- [Documentação oficial](https://playwright.dev/python/)