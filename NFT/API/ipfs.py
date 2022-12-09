import ipfsapi
import base64


def ipfs_api(Bytes: str, UserAddress: str, NFTName: str, NFTCost: str) -> str:
    """Only works with ipfs desktop running"""
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        Bytes = bytes(Bytes, encoding='utf-8')
        ipfs_hash = api.add_bytes(base64.b64decode(Bytes))
        json = str({"IpfsHash": ipfs_hash, "UserAddress": UserAddress, "NFTName": NFTName, "NFTCost": NFTCost})
        json_hash = api.add_str(json)
        return json_hash
    except AttributeError:
        return "None"
