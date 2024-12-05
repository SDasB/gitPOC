import json

import requests

target_url = "http://localhost:8080/bookingservice/bookings/bookings"

# url = "http://localhost:8080/bookingservice/bookings/bookings"
#
# payload = json.dumps({
#   "description": "Cool description!",
#   "price": 700,
#   "currency": "EUR",
#   "subscription_start_date": 6831248450011,
#   "email": "valid@email.com",
#   "department": "Gov Department"
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# r = requests.request("POST", url, headers=headers, data=payload)

response = requests.get(target_url)
# print(r)

print(f"Response Code: {response.status_code}")
print("Response Content:")
print(response.text)

jess_list = json.loads(response.text)
print(type(jess_list))

unique_departments = set(entry["department"] for entry in jess_list)
print("The values corresponding to key : " + str(unique_departments))