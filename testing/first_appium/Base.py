import os

import pytest as pytest
from appium import webdriver

from conftest import desired_caps


class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        if os.environ.get("BS_USERNAME") is None:
            # Enter LT username here if environment variables have not been added
            username = "latifa.asal2021"
        else:
            username = os.environ.get("BS_USERNAME")
        if os.environ.get("BS_ACCESS_KEY") is None:
            # Enter LT accesskey here if environment variables have not been added
            accesskey = "h91FSDuLZhjuQuDLUzxJj1OmJqPslPY00QgtulRJdHXuEPHPe5"
        else:
            accesskey = os.environ.get("BS_ACCESS_KEY")
        # Initialize the remote Webdriver using BrowserStack remote URL
        # and desired capabilities defined above
        driver = webdriver.Remote(desired_capabilities=desired_caps,
                                  command_executor="https://" + username + ":" + accesskey + "@mobile-hub.lambdatest.com/wd/hub")

        yield driver
