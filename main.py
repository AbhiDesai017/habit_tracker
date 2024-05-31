import requests
from datetime import datetime

TOKEN = "f7yq8uhf72y3g886y23ih"
USERNAME = "desi"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

res = requests.post(url=pixela_endpoint, json=user_params)
print(res.text)

# ------------------------------- Graph ---------------------------- #

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# res = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(res.text)

# ------------------------------- input - km ---------------------------- #

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# res = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
# print(res.text)

# ------------------------------- Update ---------------------------- #

update_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "18",
}

# res = requests.put(url=update_end_point, json=new_pixel_data, headers=headers)
# print(res.text)


# ------------------------------- Delete ---------------------------- #

delete_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# res = requests.delete(url=delete_end_point, headers=headers)
# print(res.text)
