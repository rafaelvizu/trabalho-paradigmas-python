class Init:
    def __init__(self) -> None:
        from src.helpers import HelpersFunc
        from src.controllers.search_products import SearchProducts

        self.email, self.password = HelpersFunc.input_login_gui()
        self.search = HelpersFunc.input_search_product_gui()

        self.email = '202202734845@alunos.estacio.br'
        self.password = 'ccff5436$'
        self.search = 'notebook'
        self.login = SearchProducts(self.email, self.password, self.search)

# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
