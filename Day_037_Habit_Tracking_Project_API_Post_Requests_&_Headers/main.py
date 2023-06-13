import requests
from datetime import datetime

# Create User

PIXELA_USERNAME = ""
PIXELA_TOKEN = ""
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response_a = requests.post(url=pixela_endpoint, json=user_params)
# print(response_a.text)


# Create a Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response_b = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response_b.text)

# Post a Pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# Can specify a specific date with datetime(year=2023, month=6, day=9)
print(today.strftime("%Y%m%d"))

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "25.5",
}

# response_c = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response_c.text)

# Update a pixel
update_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
pixel_params_update = {
    "quantity": "10.5",
}
# response_d = requests.put(url=update_pixel_endpoint, json=pixel_params_update, headers=headers)
# print(response_d.text)

# Delete a Pixel
delete_pixel_endpoint = f"{pixel_endpoint}/20230609"
# response_e = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response_e.text)
