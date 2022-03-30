from asyncio.windows_events import NULL
import requests
import unittest
import random
import string

def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(length))
    return randomString

def getToken():
    login = {
            "username": get_random_string(5),
            "password": get_random_string(5)
            }
    response = requests.post("https://dev.yuride.network/api/token/", login)
    data = response.json()
    access = data['access']
    refresh = data['refresh']
    tokens ={"access": access,
             "refresh": refresh,
             "username": login["username"],
             "password": login["password"]
            }
    return tokens

class TestYuride(unittest.TestCase):
    def test_me(self):
        tokens = getToken()
        access = {"access": tokens["access"]}
        accessToken = tokens["access"]
        headersAuth = {
            'Authorization': 'Bearer ' + str(accessToken),
        }
        response = requests.get('https://dev.yuride.network/api/users/me/', headers=headersAuth, params=access)
        data = response.json()
        username = data['username']
        self.assertEqual(username,tokens["username"])
        self.assertEqual(response.status_code, 200)

    def test_me_invalid_token(self):
        access = {"access": "ayy_lmao"}
        accessToken = "ayy_lmao"
        headersAuth = {
            'Authorization': 'Bearer ' + str(accessToken),
        }
        response = requests.get('https://dev.yuride.network/api/users/me/', headers=headersAuth, params=access)
        data = response.json()
        self.assertEqual(data["code"], "token_not_valid")
        self.assertEqual(response.status_code, 403)

    def test_me_no_token(self):
        access = {"access": "ayy_lmao"}
        accessToken = "ayy_lmao"
        headersAuth = ""
        response = requests.get('https://dev.yuride.network/api/users/me/', headers=headersAuth, params=access)
        data = response.json()
        self.assertEqual(response.status_code, 403)
        

if __name__ == "__main__":
    unittest.main()

