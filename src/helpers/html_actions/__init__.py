from src.config import Config
from selenium.webdriver.common.by import By


class HtmlActions:
    nav = Config().get_browser()

    @staticmethod
    def get_element_by_css_selector_and_click(css_selector):
        element = HtmlActions.nav.find_element(By.CSS_SELECTOR, css_selector)
        element.click()

    @staticmethod
    def get_element_by_css_selector_and_send_key(css_selector, keys):
        element = HtmlActions.nav.find_element(By.CSS_SELECTOR, css_selector)
        element.send_keys(keys)

    @staticmethod
    def get_element_by_css_selector_and_get_text(css_selector):
        element = HtmlActions.nav.find_element(By.CSS_SELECTOR, css_selector)
        return element.text

    @staticmethod
    def get_elements_by_css_selector(css_selector):
        elements = HtmlActions.nav.find_elements(By.CSS_SELECTOR, css_selector)
        return elements

    @staticmethod
    def get_element_by_css_selector_element(css_selector, element):
        return element.find_element(By.CSS_SELECTOR, css_selector)

    @staticmethod
    def switch_to_new_tab(window_number):
        HtmlActions.nav.switch_to.window(HtmlActions.nav.window_handles[window_number])
