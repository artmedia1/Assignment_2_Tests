import requests
import unittest
import random
import string

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Firefox(options=options)

def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(length))
    return randomString


class TestYuride(unittest.TestCase):
    def test_token(self):
        response = requests.get("https://dev.yuride.network/")

        login = {
        "username": "testlol1",
        "password": "testlol1pw"
        }
        response = requests.post("https://dev.yuride.network/api/token/", login)
        data = response.json()
        access = data['access']
        refresh = data['refresh']
        self.assertTrue(access)
        self.assertTrue(refresh)
        self.assertEqual(response.status_code, 200)


    def test_token_random(self):    
        for x in range(5):  
            username = get_random_string(5)
            password = get_random_string(5)
            login = {
                    "username": username,
                    "password": password
                    }
            response = requests.post("https://dev.yuride.network/api/token/", login)
            data = response.json()
            access = data['access']
            refresh = data['refresh']
            self.assertTrue(access)
            self.assertTrue(refresh)
            self.assertEqual(response.status_code, 200)

    def test_token_no_password(self):    
        login = {
                "username": "",
                "password": ""
                }
        response = requests.post("https://dev.yuride.network/api/token/", login)
        self.assertEqual(response.status_code, 400)    

    def test_token_no_body(self):    
        response = requests.post("https://dev.yuride.network/api/token/")
        self.assertEqual(response.status_code, 400)     




if __name__ == "__main__":
    unittest.main()



