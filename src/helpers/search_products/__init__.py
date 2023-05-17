from src.helpers import get_default_sleep
from src.helpers.html_actions import HtmlActions
from src.helpers import input_search_product
from src.helpers import save_xlsx_file
from time import sleep

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

        # botão de login
        HtmlActions.get_element_by_css_selector_and_click(
            '#section-login > div > div > div.sc-cNNTdL.hItoDh.colLogin > section > div.sc-gKRMOK.hWvdtC > button')

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

        # vamos ver quantos produtos temos
        products_elements = HtmlActions.get_elements_by_css_selector('.productCard')
        products_count = len(products_elements)

        # vamos acessar um por um e pegar as informações
        for i in range(0, products_count):
            product_element = products_elements[i]

            # pegar o nome do produto
            name_element = HtmlActions.get_element_by_css_selector_element('.nameCard', product_element)
            if name_element is not None:
                name = name_element.text
            else:
                name = 'Não encontrado'

            # pegar preço antigo, se houver
            old_price_element = HtmlActions.get_element_by_css_selector_element('.oldPriceCard', product_element)
            if old_price_element is not None:
                old_price = old_price_element.text
            else:
                old_price = 'Não encontrado'

            # pegar preço atual
            current_price_element = HtmlActions.get_element_by_css_selector_element('.priceCard', product_element)
            if current_price_element is not None:
                current_price = current_price_element.text
            else:
                current_price = 'Não encontrado'

            try:
                # tempo de oferta
                current_down_offer_element = HtmlActions.get_element_by_css_selector_element(
                    '.countdownOffer', product_element)

                if current_down_offer_element is not None:
                    current_down_offer = current_down_offer_element.text
                else:
                    current_down_offer = 'Não encontrado'
            except:
                current_down_offer = 'Não encontrado'

            # link do produto
            link_element = HtmlActions.get_element_by_css_selector_element('a', product_element)
            if link_element is not None:
                link = link_element.get_attribute('href')
            else:
                link = 'Não encontrado'

            # adicionar produto na lista
            self.products.append({
                'name': name,
                'old_price': old_price,
                'current_price': current_price,
                'current_down_offer': current_down_offer,
                'link': link
            })

        save_xlsx_file(self.products)
