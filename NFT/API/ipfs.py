import ipfsApi
import requests.exceptions
import base64


def ipfs_api(bts: str) -> str:
    """Only works with ipfs desktop running"""
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsApi.Client(ip, port)
        #response = api.add(bts)
        bts = bytes(bts, encoding='utf-8')
        print(base64.b64decode(bts))
        response = api.add_bytes(base64.b64decode(bts))
        with open("API/files/test.jpg", "wb") as file:
            file.write(base64.b64decode(bts))
        return response
    except AttributeError:
        return "None"


def ipfs_api_get(hash: str) -> bytes:
    try:
        ip, port = "127.0.0.1", 8080
        api = ipfsApi.Client(ip, port)
        file = api.cat(hash)
        return base64.b64encode(file)

    except:
        print("Error")