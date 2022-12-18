#GET
import requests
api_url = "https://reqres.in/api/unknown/2"
response = requests.get(api_url)
print(response.json())
response.status_code

if response.status_code == 200 : 
    print("200")

elif response.status_code == 404 :
    print("404")

elif response.status_code == 400 :
    print("400")

#POST
import requests
api_url = "https://reqres.in/api/register"
todo = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(api_url, json=todo)
print(response.json())
response.status_code

if response.status_code == 201 : 
    print("201")

elif response.status_code == 200 :
    print("200")

elif response.status_code == 400 :
    print("400")