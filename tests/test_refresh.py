import requests
import unittest
import random
import string

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Firefox(options=options)

def get_random_string(length): #Returns a random string of letters and numbers of size of input length
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(length))
    return randomString

def getToken(): #creatres a random username and password, then returns it's refresh and access tokens
    login = { #creates a JSON for the login credentials 
            "username": get_random_string(5),
            "password": get_random_string(5)
            }
    response = requests.post("https://dev.yuride.network/api/token/", login)
    data = response.json()
    access = data['access']
    refresh = data['refresh']
    tokens ={
            "access": access,
            "refresh": refresh
            }
    return tokens

def getAccessToken(refresh): #Takes a refresh token then tries to return it's access token, field code and https response code in a JSON format
    response = requests.post("https://dev.yuride.network/api/token/refresh/", refresh)
    data = response.json()
    dataDict = {}
    try:
        access = {"access": data["access"]}
        dataDict.update(access)
    except:
        pass

    try:
        code = {"code": data["code"]}
        dataDict.update(code)
    except:
        pass

    status = {"status": response.status_code}
    dataDict.update(status)
    return dataDict

class TestYuride(unittest.TestCase):
    def test_refresh(self):
        list = getToken() #Randomly generates username and password and retreives their tokens
        refresh = {"refresh":list["refresh"]}
        validateAccess = getAccessToken(refresh) #Inputs the refresh token and tries to retrieve the access token, field code and https response in JSON format
        accessToken = validateAccess["access"]
        status = validateAccess["status"]
        self.assertEqual(status, 200)
        self.assertTrue(accessToken)

    def test_refresh_no_body(self):
        refresh = ""
        validateAccess = getAccessToken(refresh) #Inputs the refresh token (empty in this case) and tries to retrieve the access token, field code and https response in JSON format
        status = validateAccess["status"]
        self.assertEqual(status, 400)

    def test_refresh_invalid_token(self):
        refresh = {"refresh": "a"} 
        validateAccess = getAccessToken(refresh) #Inputs the refresh token (invalid in this case) and tries to retrieve the access token, field code and https response in JSON format
        status = validateAccess["status"]
        code = validateAccess["code"]
        self.assertEqual(status, 401)
        self.assertEqual(code, "token_not_valid")

    
if __name__ == "__main__":
    unittest.main()


