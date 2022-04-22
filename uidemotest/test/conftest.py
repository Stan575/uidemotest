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
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1600,1080')
        if 'headless' in browser:
            options.headless = True
        else:
            options.headless = False
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()
