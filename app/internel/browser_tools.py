from selenium import webdriver
import config as CONFIG


class BrowserTools:
    browser = None
    display = None

    def getBrowser(self):


        if CONFIG.BROWSER_DRIVE is 'firefox':
            from selenium.webdriver.firefox.options import Options
            firefox_opt = Options()
            firefox_opt.headless = True
            self.browser = webdriver.Firefox(options=firefox_opt)
        if CONFIG.BROWSER_DRIVE is 'chrome':
            from selenium.webdriver.chrome.options import Options
            firefox_opt = Options()
            firefox_opt.headless = True
            self.browser = webdriver.Chrome(options=firefox_opt)

        return self.browser

    def closeBrowser(self):
        self.browser.close()
