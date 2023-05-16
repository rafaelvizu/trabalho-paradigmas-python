from config import Config
from selenium.webdriver.common.by import By
from time import sleep


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.nav = Config().get_navegador()
        self.start()

    def start(self):
        self.nav.get('https://estudante.estacio.br/login')
        sleep(2)

        # procurar o elemento
        bt = self.nav.find_element(By.CSS_SELECTOR,
            '#section-login > div > div > div > section > div.sc-gKRMOK.hWvdtC > button')
        bt.click()

        sleep(2)

        form_email = self.nav.find_element(By.CSS_SELECTOR, '#i0116')
        # colocar o email
        form_email.send_keys(self.email)

        btn_proximo = self.nav.find_element(By.CSS_SELECTOR, '#idSIButton9')
        btn_proximo.click()

        sleep(2)

        form_password = self.nav.find_element(By.CSS_SELECTOR, '#i0118')

        # colocar a senha
        form_password.send_keys(self.password)

        btn_entrar = self.nav.find_element(By.CSS_SELECTOR, '#idSIButton9')
        btn_entrar.click()

        # continuar conectado? Não
        btn_nao = self.nav.find_element(By.CSS_SELECTOR, '#idBtn_Back')
        btn_nao.click()

        sleep(50)
