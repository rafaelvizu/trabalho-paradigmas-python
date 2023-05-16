from time import sleep
from src.helpers import get_default_sleep
from src.helpers.html_actions import HtmlActions
from src.helpers import input_search_product
from src.helpers import save_xlsx_file

DEFAULT_SLEEP = get_default_sleep()


class SearchProducts:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.products = list()

        # fazer operações com o navegador
        self._login()
        self._access_link()
        self._get_product()
        HtmlActions.nav.close()


    def _login(self):
        HtmlActions.nav.get('https://estudante.estacio.br/login')
        sleep(DEFAULT_SLEEP)

        # botão de search_products
        HtmlActions.get_element_by_css_selector_and_click(
            '#section-search_products > div > div > div > section > div.sc-gKRMOK.hWvdtC > button')
        sleep(DEFAULT_SLEEP)

        # colocar o email
        HtmlActions.get_element_by_css_selector_and_send_key('#i0116', self.email)

        # botão de continuar
        HtmlActions.get_element_by_css_selector_and_click('#idSIButton9')
        sleep(DEFAULT_SLEEP)

        # colocar a senha
        HtmlActions.get_element_by_css_selector_and_send_key('#i0118', self.password)
        HtmlActions.get_element_by_css_selector_and_click('#idSIButton9')
        sleep(DEFAULT_SLEEP)

        # continuar conectado? Não
        HtmlActions.get_element_by_css_selector_and_click('#idBtn_Back')
        sleep(DEFAULT_SLEEP)

    def _access_link(self):
        sleep(DEFAULT_SLEEP / 2)

        # acessar disciplina
        HtmlActions.get_element_by_css_selector_and_click('#card-entrega-ARA0066 > header > button')
        sleep(DEFAULT_SLEEP)

        # acessar sessão da atividade
        HtmlActions.get_element_by_css_selector_and_click('#segunda-tab')
        sleep(DEFAULT_SLEEP)

        # acessar atividade
        HtmlActions.get_element_by_css_selector_and_click('#acessar-conteudo-complementar-link-646160d3efeb4f0025211737')
        sleep(DEFAULT_SLEEP)

        # pegar nova aba aberta
        HtmlActions.switch_to_new_tab(1)

    def _get_product(self):
        # pesquisar produto
        search = input_search_product()
        HtmlActions.get_element_by_css_selector_and_send_key('#input-busca', search)
        HtmlActions.get_element_by_css_selector_and_click('#barraBuscaKabum > div > form > button')

        sleep(DEFAULT_SLEEP)
        old_prices_elements = HtmlActions.get_elements_by_css_selector(
            'div.availablePricesCard > .oldPriceCard')
        current_prices_elements = HtmlActions.get_elements_by_css_selector(
            'div.availablePricesCard > span.priceCard')
        names_elements = HtmlActions.get_elements_by_css_selector(
            'main > div > a > div > button > div > h2 > span.nameCard')

        old_prices = list()
        current_prices = list()
        names = list()

        for element in old_prices_elements:
            if element.text != '':
                old_prices.append(element.text)
                continue
            old_prices.append(None)

        for element in current_prices_elements:
            if element.text != '':
                current_prices.append(element.text)
                continue
            current_prices.append(None)

        for element in names_elements:
            if element.text != '':
                names.append(element.text)
                continue
            names.append(None)

        for i in range(len(names)):
            self.products.append({
                'name': names[i],
                'old_price': old_prices[i],
                'current_price': current_prices[i],
            })

        save_xlsx_file(self.products)
