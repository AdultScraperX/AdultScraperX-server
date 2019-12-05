from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import config as CONFIG


class BrowserTools:
    browser = None
    display = None

    def getBrowser(self):
        firefox_opt = Options()
        firefox_opt.headless = True

        if not CONFIG.REMOTE_WEB:
            self.browser = webdriver.Firefox(options=firefox_opt)

        else:
            self.browser = webdriver.Remote(
                command_executor='http://' + CONFIG.WEB_DRIVE_URL + ':' + CONFIG.WEB_DRIVE_PORT + '/wd/hub',
                # selenium为docker-compose的host名
                desired_capabilities=DesiredCapabilities.FIREFOX,
                options=firefox_opt)
        return self.browser

    def closeBrowser(self):
        self.browser.close()
