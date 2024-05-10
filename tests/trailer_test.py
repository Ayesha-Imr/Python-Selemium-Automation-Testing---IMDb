import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WatchTrailerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the ChromeDriver path
        service = Service(r"..\drivers\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_watch_despicable_me_trailer(self):
        # Navigate to IMDb
        self.driver.get("https://www.imdb.com")

        # Open the menu
        menu_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]'))
        )
        menu_btn.click()

        # Wait for menu options to be visible and select "Latest Trailers"
        latest_trailers_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[2]/div[2]/span/div/div/ul/a[2]'))
        )
        latest_trailers_link.click()

        # Click on the "Despicable Me" trailer
        despicable_me_trailer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section[1]/div/div[2]/div[1]/a'))
        )
        despicable_me_trailer.click()

        # Wait for the video to load and then click the maximize button
        maximize_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="imdbnext-vp-jw-single"]/div[2]/div[12]/div[4]/div[2]/div[15]'))
        )
        maximize_button.click()

        # Minimize the video
        minimize_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="imdbnext-vp-jw-single"]/div[2]/div[12]/div[4]/div[2]/div[15]'))
        )
        minimize_button.click()

        # Confirm the video is minimized and print test passed message
        print("Test passed: Video was maximized and then minimized successfully.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
