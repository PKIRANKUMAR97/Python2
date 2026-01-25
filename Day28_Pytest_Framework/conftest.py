import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




    elif browser == "firefox":
        driver = webdriver.Firefox()



    elif browser == "edge":
        service_obj = Service(r"C:\browserdrivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    else:
        raise ValueError(f"Invalid browser name: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):  ## it will capture the value we pass through the command line
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome / firefox / edge"
    )


@pytest.fixture()
def browser(request): ## this will return the value of the browser to the setup method
    return request.config.getoption("--browser")


