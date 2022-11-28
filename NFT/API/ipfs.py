import ipfsApi
import requests.exceptions
import base64


def ipfs_api(bts: str) -> str:
    """Only works with ipfs desktop running"""
    try:
        """data for connect to ipfs"""
        ip, port = "127.0.0.1", 5001
        api = ipfsApi.Client(ip, port)

        """convert bts string to bytes"""
        bts = bytes(bts, encoding='utf-8')

        """decode file and add it to ipfs"""
        response = api.add_bytes(base64.b64decode(bts))

        """return string with file cid"""
        return response

    except AttributeError:
        return "None"


def ipfs_api_get(cid: str) -> bytes:
    try:
        """data for connect to ipfs"""
        ip, port = "127.0.0.1", 8080
        api = ipfsApi.Client(ip, port)

        """get file from ipfs"""
        file = api.cat(cid)

        """return encoded to base64 file"""
        return base64.b64encode(file)

    except:
        print("Error")