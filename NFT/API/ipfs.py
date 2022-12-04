import ipfsapi
import base64


def ipfs_api(bts: str) -> str:
    """Only works with ipfs desktop running"""
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        bts = bytes(bts, encoding='utf-8')
        print(bts)
        response = api.add_bytes(base64.b64decode(bts))
        return response
    except AttributeError:
        return "None"