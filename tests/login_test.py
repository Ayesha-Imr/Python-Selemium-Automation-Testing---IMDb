import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogInTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Correctly set up the ChromeDriver path
        service = Service(r"..\drivers\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_log_in(self):
        # Navigate to the IMDb login page
        self.driver.get(r"https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")  

        # Fill out the login form
        email_field = self.driver.find_element(By.XPATH, '//*[@id="ap_email"]')
        email_field.send_keys("ayesha.ml2002@gmail.com")  # Email used for login

        password_field = self.driver.find_element(By.XPATH, '//*[@id="ap_password"]')
        password_field.send_keys("sampleSQE#test123")  # Password used for login

        # Click the 'Sign In' button
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
        sign_in_button.click()

        # Assuming that reaching here means the button was successfully clicked
        print("Log in successful - test passed.")

    def test_failed_log_in(self):
        # Navigate to the IMDb login page
        self.driver.get(r"https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")  

        # Fill out the login form
        email_field = self.driver.find_element(By.XPATH, '//*[@id="ap_email"]')
        email_field.send_keys("ayesha.ml2002@gmail.com")  # Email used for login

        password_field = self.driver.find_element(By.XPATH, '//*[@id="ap_password"]')
        password_field.send_keys("incorrectpassword")  # Incorrect password used for login

        # Click the 'Sign In' button
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
        sign_in_button.click()

        # Assuming that reaching here means the button was successfully clicked
        print("Failed login attempt - test passed.")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
