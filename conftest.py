import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse=True)
def init_driver(request):
    driver = None
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', "headlessfirefox"]

    browser = 'ch'
    browser = browser.lower()

    if browser not in supported_browsers:
        raise RuntimeError(f'Provided browser "{browser}" is not supported.\n'
                           f'\t\tSupported browsers are: {str(supported_browsers)[1:-1]}.')

    if 'ch' in browser:
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
        elif 'headless' in browser:
            chrome_options.headless = True
        else:
            chrome_options.headless = False
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()
