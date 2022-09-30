import time

from Pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def selectHyundai(self):
        self.click("Hyundai_XPATH")


    def selectToyota(self):
        self.click("toyota_XPATH")
        time.sleep(1)

    def selectBMW(self):
        self.click("BMW_XPATH")
        time.sleep(1)

    def selectHonda(self):
        self.click("honda_XPATH")
        time.sleep(1)
