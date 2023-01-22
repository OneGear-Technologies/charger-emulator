import requests
from requests_toolbelt.adapters import source
import time
import qrcode

cid = 100
uid = 90876543211

img = qrcode.make(cid)
#img.save("test.png")
img.show()

headers = {
     "Content-Type" : "application/json"
}
data = {
    "uid" : uid,
    "cid" : cid
}

while True:
    r = requests.request("POST", "http://0.0.0.0:8000/charge/get-stat/", headers=headers, json=data)
    print(f"Charge { cid }'s status: ", end="")
    if r.json()['charge_stat']:
        print("Unlocked/Charging")
    else:
        print("Locked/Not Charging")

    time.sleep(20)
