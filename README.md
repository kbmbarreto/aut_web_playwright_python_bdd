# aut_web_playwright_python_bdd

<p>Exemplo de automação em Python utilizando BDD, para fins acadêmicos e aprendizado do Playwright</p>

## Ferramentas utilizadas

- Python 3.12
- Playwright 1.47.0
- Behave 1.2.6
- Allure Report 2.13.5


## Execução dos testes com o Behave
Para executar os testes sem utilizar o Allure:

<br>`behave` -> executa os testes com o Behave.
<br>`behave features/nome_do_arquivo.feature` -> executa os testes de um arquivo de feature específico.
<br>`behave -n "Nome do Cenário"` -> executa os testes pelo nome do cenário.
<br>`behave -t @login` -> executa os testes com uma tag específica.


## Execução dos testes com o Allure Reports
Antes de executar os testes, precisamos instalar o Allure CLI:

Instalação no ambiente Windows utilizando o Scoop:
<br>`scoop install allure`;

Instalação no ambiente MacOS utilizando o HomeBrew:
<br>`brew install allure`;


Para executar os testes gerando o relatório do Allure, utilize os comandos a seguir na raiz do projeto:

<br>`behave -f allure_behave.formatter:AllureFormatter -o allure-results` -> executa todos os testes e cria os 
relatórios do Allure;
<br>`allure serve allure-results` -> executa o relatório com o servidor do Allure;
<br>`allure generate allure-results -o allure-report --clean` -> pode utilizar este comando para gerar o relatório em 
HTML sem executar no servidor do Allure.


## Documentação do projeto.
````
aut_web_playwright_navpro/
├── .venv/
├── features/
│   ├── steps/
│   │   ├── cadastro_steps.py
│   │   ├── common_steps.py
│   │   ├── landing_steps.py
│   │   └── login_steps.py
│   ├── cadastro.feature
│   ├── environment.py
│   ├── landing.feature
│   └── login.feature
├── page_objects/
│   ├── actions/
│   │   ├── cadastro_page.py
│   │   ├── landing_page.py
│   │   └── login_page.py
│   ├── elements/
│   │   ├── cadastro_locators.py
│   │   ├── landing_locators.py
│   │   └── login_locators.py
├── support/
│   └── utils.py
├── .gitignore
├── conftest.py
├── README.md
└── requirements.txt
````

- [Documentação oficial](https://playwright.dev/python/)