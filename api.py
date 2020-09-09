# for making requests
import requests


https = false

host = "localhost"

port = 8080

if https:
    host = "https://" + host
else:
    host = "http://" + host

def get_url(req):
    req = req.lower()
    if req == "install":
        return host + ":" + str(port) + "/install"


def install(name, version="latest"):


