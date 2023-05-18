from src.helpers.html_actions import HtmlActions
from src.helpers import HelpersFunc
from time import sleep

DEFAULT_SLEEP = 5


class SearchProducts:
    def __init__(self, email, password, search):
        self.email = email
        self.password = password
        self.search = search
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
        HtmlActions.get_element_by_css_selector_and_click(
            '#acessar-conteudo-complementar-link-646160d3efeb4f0025211737')
        sleep(DEFAULT_SLEEP)

        # pegar nova aba aberta
        HtmlActions.switch_to_new_tab(1)

    def _get_product(self):
        # pesquisar produto
        HtmlActions.get_element_by_css_selector_and_send_key('#input-busca', self.search)
        HtmlActions.get_element_by_css_selector_and_click('#barraBuscaKabum > div > form > button')

        sleep(DEFAULT_SLEEP)

        # ordenar por preço crescente
        HtmlActions.get_element_by_css_selector_and_click(
            '#Filter > div.sc-8c5ed0b2-1.eNJXYl > select > option:nth-child(2)')

        sleep(DEFAULT_SLEEP)

        # colocar 100 produtos por página
        HtmlActions.get_element_by_css_selector_and_click('#Filter > label > select > option:nth-child(5)')
        sleep(DEFAULT_SLEEP)

        # vamos ver quantos produtos temos
        products_elements = HtmlActions.get_elements_by_css_selector('.productCard')
        products_count = len(products_elements)

        # vamos acessar um por um e pegar as informações
        for i in range(0, products_count):
            product_element = products_elements[i]

            # vamos pegar o nome do produto
            product_name = HtmlActions.get_element_by_css_selector_element(
                '.nameCard', product_element)

            if product_name is None:
                product_name = 'Produto sem nome'
            else:
                product_name = product_name.text

            try:
                # vamos o tempo de promoção
                product_promotion_time = HtmlActions.get_element_by_css_selector_element(
                    '.countdownOffer', product_element)

                if product_promotion_time is not None:
                    product_promotion_time = product_promotion_time.text
            except:
                product_promotion_time = None

            # vamos pegar o preço original do produto
            if product_promotion_time is None:
                product_price = HtmlActions.get_element_by_css_selector_element(
                    '.priceCard', product_element)
            else:
                product_price = HtmlActions.get_element_by_css_selector_element(
                    '.oldPriceCard', product_element)

            product_price = product_price.text.replace('R$', '')
            product_price = product_price.replace('.', '')
            product_price = product_price.replace(',', '.')
            product_price = product_price.replace(' ', '')

            if product_price == '---' or product_price is None or not product_price:
                product_price = -1
            else:
                product_price = float(product_price)

            # vamos pegar o preço promocional do produto
            if product_promotion_time is not None:
                product_promotion_price = HtmlActions.get_element_by_css_selector_element(
                    '.priceCard', product_element)
                product_promotion_price = product_promotion_price.text.replace('R$', '')
                product_promotion_price = product_promotion_price.replace('.', '')
                product_promotion_price = product_promotion_price.replace(',', '.')
                product_promotion_price = product_promotion_price.replace(' ', '')

                if product_promotion_price is None:
                    product_promotion_price = None
            else:
                product_promotion_price = None

            # pegar link do produto
            product_link = HtmlActions.get_element_by_css_selector_element(
                'a', product_element)
            product_link = product_link.get_attribute('href')

            self.products.append({
                'name': product_name,
                'promotion_time': product_promotion_time,
                'price': product_price,
                'promotion_price': product_promotion_price,
                'link': product_link
            })

        HelpersFunc.save_xlsx_file(self.products)

# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
