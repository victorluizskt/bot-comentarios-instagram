import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path='geck/geckodriver')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        # botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # botao_login.click()
        time.sleep(10)
        campo_usuario = driver.find_element_by_xpath('//input[@name="username"]')
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath('//input[@name="password"]')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comentarios()

    @staticmethod
    def person(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5) / 30)

    def comentarios(self):
        totalCom = 0
        driver = self.driver
        driver.get("Link para coméntarios")
        time.sleep(5)
        while True:
            try:
                comentarios = ["Comentário que deseja fazer."]
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                campo_comentario.click()
                time.sleep(random.randint(7, 15))
                self.person(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(15, 22))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(20)
                totalCom += 1
            except:
                print(totalCom)


botComentarios = InstagramBot('Seu username', 'Sua senha')
botComentarios.login()
