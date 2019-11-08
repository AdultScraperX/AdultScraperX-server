import platform
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class BrowserTools:
    browser = None
    display = None

    def getBrowser(self):
        firefox_opt = Options()
        firefox_opt.add_argument('--headless')
        firefox_opt.add_argument('--disable-gpu')
        sysStr = platform.system()

        if sysStr == "Linux":
            # linux 使用虚拟屏幕
            from pyvirtualdisplay import Display
            self.display = Display(visible=0, size=(800, 600))
            self.display.start()

        self.browser = webdriver.Firefox(firefox_options=firefox_opt)
        return self.browser

    def closeBrowser(self):
        sysStr = platform.system()
        self.browser.close()
        if sysStr == "Linux":
            # linux 使用虚拟屏幕
            self.display.stop()
