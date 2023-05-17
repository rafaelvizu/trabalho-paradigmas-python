# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
from src import Init


if __name__ == '__main__':
    try:
        Init()
    except Exception as e:
        print('Ocorreu um erro inesperado!', e)
