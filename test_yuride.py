import requests
import json
import pprint
import unittest
import selenium
import time as t
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



class TestYuride(unittest.TestCase):
    def test_ping(self):
        response = requests.get("https://dev.yuride.network/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

r = requests.get("https://dev.yuride.network/api/token/")

test = r.json()

print(test)