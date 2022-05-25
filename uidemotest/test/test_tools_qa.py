import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://demoqa.com'


class TestToolsQANavigation(unittest.TestCase):
    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        if 'CICD_RUN' in os.environ:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 8)
        self.driver.get(BASE_URL)

    def test_navigate_to_toolsQA(self):
        self.assertEqual(self.driver.title, 'ToolsQA')

    def test_logo(self):
        logo_image = self.driver.find_element(By.XPATH, '//header//img')
        self.assertTrue(logo_image.is_displayed())

    def test_elements_link(self):
        elements_card = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='Elements']")))
        elements_card.click()
        self.assertEqual(self.driver.current_url, f'{BASE_URL}/elements')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()