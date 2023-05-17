import os
import xlsxwriter
from datetime import datetime
import tkinter as tk


class HelpersFunc:
    @staticmethod
    def input_login_gui():
        window = tk.Tk()
        # tela de login com os componentes grandes e bonitos
        window.title('Login')
        window.geometry('240x200')
        window.configure(background='white')

        # componentes
        label_email = tk.Label(window, text='Email', bg='white', fg='black')
        label_email.place(x=10, y=10)
        entry_email = tk.Entry(window, width=30, font=('Arial', 10))
        entry_email.place(x=10, y=30)
        entry_email.focus()

        label_password = tk.Label(window, text='Senha', bg='white', fg='black')
        label_password.place(x=10, y=60)
        entry_password = tk.Entry(window, width=30, show='*', font=('Arial', 10))
        entry_password.place(x=10, y=80)

        button_login = tk.Button(window, text='Login', width=25, command=window.quit, font=('Arial', 10))
        button_login.place(x=10, y=120)

        window.mainloop()

        emailData = entry_email.get().strip()
        passworData = entry_password.get()
        window.destroy()

        return emailData, passworData

    @staticmethod
    def input_search_product_gui():
        window = tk.Tk()

        window.title('Pesquisar produto')
        window.geometry('240x200')
        window.configure(background='white')

        label_search = tk.Label(window, text='Pesquisar produto', bg='white', fg='black')
        label_search.place(x=10, y=10)
        entry_search = tk.Entry(window, width=30, font=('Arial', 10))
        entry_search.place(x=10, y=30)
        entry_search.focus()

        button_search = tk.Button(window, text='Pesquisar', width=25, command=window.quit, font=('Arial', 10))
        button_search.place(x=10, y=120)

        window.mainloop()

        searchData = entry_search.get().strip()
        window.destroy()

        return searchData

    @staticmethod
    def save_xlsx_file(products):
        HelpersFunc.create_path_data_if_not_exists()
        workbook = xlsxwriter.Workbook(f'data/products-{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.xlsx')
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

        path = os.path.abspath(workbook.filename)
        print(f'Arquivo salvo em: {path}')

        os.startfile('data')
        workbook.close()

    @staticmethod
    def create_path_data_if_not_exists():
        if not os.path.exists('data'):
            os.mkdir('../data')

# Autor: Rafael Vizú - https://github.com/rafaelvizu/trabalho-paradigmas-python/
