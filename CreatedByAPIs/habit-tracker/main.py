import requests
import datetime
import os

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "jeongbeenson"
GRAPH_ID = "graph1"
TODAY = datetime.date.today().strftime("%Y%m%d")
GRAPH_ADDRESS = "https://pixe.la/v1/users/jeongbeenson/graphs/graph1.html"

# Create a user
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "JB's running habit tracker",
    "unit": "Kilometer(s)",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Seoul",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Post a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": TODAY,
    "quantity": "0.8",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# Update a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

update_pixel_config = {
    "quantity": "1.0",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# Delete a pixel
delete_pixel_endpoint = update_pixel_endpoint

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
