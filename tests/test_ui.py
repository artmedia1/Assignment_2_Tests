import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)


class TestYuride(unittest.TestCase):
    def test_ui(self):
        driver.get("https://dev.yuride.network")
        self.assertEqual(driver.title, "Your Website")
        element=driver.find_element(By.XPATH,"/html/body/section/div/div[2]/div[1]/a")
        element.click()

        try:     
            WebDriverWait(driver,600).until(EC.presence_of_element_located((By.ID, "york-logo")))
        except:
            print("Webpage took longer than 10 minutes to load")

        element=driver.find_element(By.ID,"mli")
        
        element.send_keys("USERNAME")
        element=driver.find_element(By.ID,"password")
        element.send_keys("PASSWORD")
        element=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input")
        element.click()
        driver.switch_to.frame(driver.find_element(By.ID, "duo_iframe"))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.auth-button:nth-child(3)'))).click()
        driver.switch_to.default_content()
        WebDriverWait(driver, 60).until(EC.title_is("Your Website"))
        element = driver.find_element(By.XPATH, "/html/body/section/div/h1")
        self.assertEqual(element.text, "DASHBOARD")
        

        
if __name__ == "__main__":
    unittest.main()
