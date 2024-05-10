import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchMovieTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the ChromeDriver path
        service = Service(r"..\drivers\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_search_movie(self):
        # Navigate to the IMDb homepage
        self.driver.get("https://www.imdb.com/?ref_=nv_home")

        # Locate the search bar and enter the movie name
        search_bar = self.driver.find_element(By.XPATH, '//*[@id="suggestion-search"]')
        search_bar.send_keys("The Lion King")

        # Click the search icon
        search_icon = self.driver.find_element(By.XPATH, '//*[@id="suggestion-search-button"]')
        search_icon.click()

        # Click on the 1994 'The Lion King' movie link from the results
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[3]/div[2]/div/a'))
        ).click()

        # Validate the test by checking for the movie's title on its page
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span'))
        )
        title_element = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span')
        assert "The Lion King" in title_element.text
        print("Test passed: The Lion King page is displayed.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
