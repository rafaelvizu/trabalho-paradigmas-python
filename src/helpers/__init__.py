import os
import xlsxwriter
from datetime import datetime


def input_search_product():
    while True:
        try:
            search = str(input('Digite o nome do produto: ')).strip()

            if len(search) == 0:
                raise ValueError('Digite um nome válido')

            continue_search = str(input('Deseja  confirmar? [S/N] ')).upper()[0]

            if continue_search == 'S':
                return search
            elif continue_search == 'N':
                continue
            else:
                raise ValueError('Digite uma opção válida')

        except ValueError as e:
            print(e)
            continue
        finally:
            print('--' * 20)


def input_login():
    while True:
        try:
            email = str(input('Digite o seu email: ')).strip()
            password = str(input('Digite a sua senha: ')).strip()

            if len(email) == 0 or len(password) == 0:
                raise ValueError('Digite um email e senha válidos')

            continue_search = str(input('Deseja  confirmar? [S/N] ')).upper()[0]

            if continue_search == 'S':
                return email, password
            elif continue_search == 'N':
                continue
            else:
                raise ValueError('Digite uma opção válida')

        except ValueError as e:
            print(e)
            continue
        finally:
            print('--' * 20)


def save_xlsx_file(products):
    create_path_data_if_not_exists()
    workbook = xlsxwriter.Workbook(f'../data/products-{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 50)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 50)

    worksheet.write('A1', 'Nome do produto')
    worksheet.write('B1', 'Preço do produto')
    worksheet.write('C1', 'Preço promocional do produto')
    worksheet.write('D1', 'Tempo de promoção do produto')
    worksheet.write('E1', 'Link do produto')

    for i in range(0, len(products)):
        product = products[i]
        worksheet.write(f'A{i + 2}', product['name'])
        worksheet.write(f'B{i + 2}', product['price'])
        worksheet.write(f'C{i + 2}', product['promotion_price'])
        worksheet.write(f'D{i + 2}', product['promotion_time'])
        worksheet.write(f'E{i + 2}', product['link'])

    print(f'Arquivo salvo com sucesso! em {workbook.filename}')
    workbook.close()


def create_path_data_if_not_exists():
    if not os.path.exists('../data'):
        os.mkdir('../data')

# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
