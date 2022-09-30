import time

import pytest

from Pages.CarBase import CarBase
from Pages.NewCarsPage import NewCarsPage
from Utilities import dataProvider
from Pages.HomePage import HomePage
from Testcases.BaseTest import BaseTest


import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("******Inside New Car Test*********")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle",
                             dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("Car brand is: ", carBrand)
        if carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("car title is: "+title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        time.sleep(3)

    @pytest.mark.parametrize("carBrand, carTitle",
                             dataProvider.get_data("NewCarsTest"))
    def test_printCarNamesAndPrices(self, carBrand, carTitle):
        log.logger.info("******Inside Car Names and Prices Testt*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("Car brand is: ", carBrand)
        if carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("car title is: " + title).encode("utf8"))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print(("car title is: " + title).encode("utf8"))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print(("car title is: " + title).encode("utf8"))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print(("car title is: " + title).encode("utf8"))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrices()




