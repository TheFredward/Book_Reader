import requests

user_email = input("type email: ")
user_pass = input("type pass: ")
response = requests.post("https://api.j-novel.club/api/users/login?include=user")
print(response)
print("----")
response2 = requests.post("https://api.j-novel.club/api/users/login?include=user",
                          data={"email": user_email, 'password': user_pass})
print(response2)
