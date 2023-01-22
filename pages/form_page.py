import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = 'Yulia'
        last_name = 'Churzina'
        email = 'julchurzina@mail.ru'
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys('8905674832')
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(
            r'C:\Users\User\PycharmProjects\ui tests sunny\text.txt.py')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('City, 1234, USA')
        self.element_is_visible(Locators.SUBMIT).click()
        return first_name, last_name, email

    def form_result(self):
        result_list = self.element_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        return result_text
