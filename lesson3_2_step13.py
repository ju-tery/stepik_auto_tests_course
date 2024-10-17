from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
        input3.send_keys("mail@mail.ru")
        input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control first']")
        input4.send_keys("+79777777777")
        input5 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control second']")
        input5.send_keys("Russia, Moscow")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_reg2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
        input3.send_keys("mail@mail.ru")
        input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control first']")
        input4.send_keys("+79777777777")
        input5 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control second']")
        input5.send_keys("Russia, Moscow")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()

