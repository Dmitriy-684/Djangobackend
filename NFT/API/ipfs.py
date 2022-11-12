import ipfsApi
import requests.exceptions


def ipfs_api(bts: tuple) -> str:
    """Only works with ipfs desktop running"""
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsApi.Client(ip, port)
        response = api.add(bts)
        return api.cat(response["Hash"])
    except AttributeError:
        return "None"