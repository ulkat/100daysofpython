import requests
from datetime import datetime
USER_NAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_params = {"id":GRAPH_ID,
                "name":"My Coding Graph",
                "unit":"h",
                "type":"float",
                "color":"shibafu",
}
headers = {
    "X-USER-TOKEn": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

point_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=7, day=25)

point_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5",
}

# response = requests.post(url=point_endpoint, json=point_params, headers=headers)
# print(response.text)

new_pixel_endpoint = f"{point_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "6"
}

# response = requests.put(url=new_pixel_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=new_pixel_endpoint, headers=headers)
# print(response.text)