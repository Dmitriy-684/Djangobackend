import ipfsApi
import requests.exceptions
import base64


def ipfs_api(bts: str) -> str:
    """Only works with ipfs desktop running"""
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsApi.Client(ip, port)
        #response = api.add(bts)
        bts = bytes(bts[2:-1], encoding='utf-8')
        print(bts[:40])

        response = api.add_bytes(base64.b64decode(bts))
        with open("API/files/test.jpg", "wb") as file:
            file.write(base64.b64decode(bts))
        return response
    except AttributeError:
        return "None"
