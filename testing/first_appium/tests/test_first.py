import time

import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testing.first_appium.Base import Base


@pytest.mark.usefixures('set_up')
class TestSample(Base):
    def test_app(self):
        driver = self.driver
        colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
        colorElement.click()

        textElement = WebDriverWait(driver, 20).until(

            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))

        textElement.click()

        toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
        toastElement.click()

        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
        notification.click()

        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()
        time.sleep(5)

        driver.back()

        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()

        speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()
        time.sleep(5)

        driver.back()

        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/webview")))
        browser.click()

        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/find")))
        find.click()
        driver.quit()
        # except:
        driver.quit()
