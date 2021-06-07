from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep


class Instragram:
    def __init__(self, username, password) -> None:
        url = "https://www.instagram.com/"
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        sleep(5)
        email = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        email.send_keys(self.username)
        password.send_keys(self.password)
        login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login.click()

    def search(self, name):
        driver = self.driver
        self.name = name
        sleep(3)
        searchBar = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]')
        inputBar = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')

        searchBar.click()
        inputBar.send_keys(name)
        sleep(3)
        inputBar.send_keys(Keys.ENTER)
        inputBar.send_keys(Keys.ENTER)
        sleep(3)

    def follow(self):
        driver = self.driver
        sleep(2)
        try:
            followBtn = driver.find_element_by_class_name("_5f5mN")
            followBtn.click()
        except:
            print(self.name + " is skipped due to some error")
            return
