from selenium import webdriver
import time

class TestWeb():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.driver = webdriver.Chrome()

    def registrar(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/usuarios/cadastro')

        driver.find_element_by_xpath('//*[@id="nome"]').send_keys(self.nome)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="senha1"]').send_keys(self.senha)
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(self.senha)

        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/form/div/div[5]/button').click()

    def login(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(self.senha)

        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/form/div/div[3]/button').click()

test = TestWeb('Jaca1234324', 'jaca1233434@gmail.com', 'jaca123')
test.registrar()
test.login()