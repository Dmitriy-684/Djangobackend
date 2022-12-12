import ipfsapi


def ipfs_load_json(bs64_image: str, UserAddress: str, NFTName: str, NFTCost: str) -> str:
    """Only works with ipfs desktop running"""
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        json = str({"bs64_image": bs64_image.replace('\'', '').replace('b', '', 1), "UserAddress": UserAddress, "NFTName": NFTName, "NFTCost": NFTCost})
        json_hash = api.add_str(json)
        return json_hash
    except AttributeError:
        return "None"


def ipfs_get_json(hash: str):
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        json = api.get_json(hash)
        return json
    except AttributeError:
        return "None"
