class Init:
    def __init__(self) -> None:
        from src.helpers import HelpersFunc

        self.email, self.password = HelpersFunc.input_login_gui()
        self.search = HelpersFunc.input_search_product_gui()
        self._start()

    def _start(self):
        from src.controllers.search_products import SearchProducts
        from time import sleep
        SearchProducts(self.email, self.password, self.search)


# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
