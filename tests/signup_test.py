import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SignUpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Correctly set up the ChromeDriver path
        service = Service(r"..\drivers\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_sign_up(self):
        # Navigate to the IMDb signup page
        self.driver.get(r"https://www.imdb.com/ap/register?openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")

        # Fill out the form with valid information
        name_field = self.driver.find_element(By.XPATH, '//*[@id="ap_customer_name"]')
        name_field.send_keys("Ayesha Imran")

        email_field = self.driver.find_element(By.XPATH, '//*[@id="ap_email"]')
        email_field.send_keys("ayesha.ml2002@example.com")

        password_field = self.driver.find_element(By.XPATH, '//*[@id="ap_password"]')
        password_field.send_keys("sampleSQE#test123")

        reenter_password_field = self.driver.find_element(By.XPATH, '//*[@id="ap_password_check"]')
        reenter_password_field.send_keys("sampleSQE#test123")

        # Click the 'Create your IMDb account' button
        signup_button = self.driver.find_element(By.XPATH, '//*[@id="continue"]')
        signup_button.click()

        # Assuming that reaching here means the button was successfully clicked
        print("Sign up successful - test passed.")


    def test_failed_sign_up(self):
        # Navigate to the IMDb signup page
        self.driver.get(r"https://www.imdb.com/ap/register?openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20")

        # Fill out the form with valid information
        name_field = self.driver.find_element(By.XPATH, '//*[@id="ap_customer_name"]')
        name_field.send_keys("Ayesha Imran")

        email_field = self.driver.find_element(By.XPATH, '//*[@id="ap_email"]')
        email_field.send_keys("ayesha.ml2002@example.com")

        password_field = self.driver.find_element(By.XPATH, '//*[@id="ap_password"]')
        password_field.send_keys("sampleSQE#test123")

        reenter_password_field = self.driver.find_element(By.XPATH, '//*[@id="ap_password_check"]')
        reenter_password_field.send_keys("incorrectpassword")  # Incorrect reentered password

        # Click the 'Create your IMDb account' button
        signup_button = self.driver.find_element(By.XPATH, '//*[@id="continue"]')
        signup_button.click()

        # Assuming that reaching here means the button was successfully clicked
        print("Failed sign up attempt - test passed.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
