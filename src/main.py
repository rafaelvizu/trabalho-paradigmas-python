# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
from controllers.search_products import SearchProducts
from helpers import input_login


if __name__ == '__main__':
    email, password = input_login()
    login = SearchProducts(email, password)
