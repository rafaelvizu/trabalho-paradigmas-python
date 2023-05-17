import os
from dotenv import load_dotenv
import xlsxwriter
from datetime import datetime


def get_default_sleep():
    load_dotenv()
    return float(os.getenv('DEFAULT_SLEEP'))


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


def save_xlsx_file(products):
    create_path_data_if_not_exists()
    workbook = xlsxwriter.Workbook(f'data/products-{ datetime.now().strftime("%d-%m-%Y-%H-%M-%S") }.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Nome')
    worksheet.write('B1', 'Preço anterior')
    worksheet.write('C1', 'Tempo de oferta')
    worksheet.write('D1', 'Preço atual')
    worksheet.write('E1', 'Link')

    worksheet.set_column('A:A', 50)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 50)


    for i in range(len(products)):
        worksheet.write(f'A{i + 2}', products[i]['name'])
        worksheet.write(f'B{i + 2}', products[i]['old_price'])
        worksheet.write(f'C{i + 2}', products[i]['current_down_offer'])
        worksheet.write(f'D{i + 2}', products[i]['current_price'])
        worksheet.write(f'E{i + 2}', products[i]['link'])

    workbook.close()


def create_path_data_if_not_exists():
    if not os.path.exists('data'):
        os.mkdir('data')
