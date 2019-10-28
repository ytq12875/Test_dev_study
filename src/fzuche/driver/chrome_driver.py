from time import sleep

from selenium import webdriver


class PageDriver:
    _path = "/home/ytq/webdriver/78.0.3904.70/chromedriver"
    _com_url = "http://10.90.136.105:23024/zugou-management/login.html"

    def __init__(self):
        self.driver = webdriver.Chrome(self._path)
        self.driver.get(self._com_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def quit_driver(self):
        self.driver.quit()

if __name__ == '__main__':
    po = PageDriver()
    sleep(5)
    po.quit_driver()