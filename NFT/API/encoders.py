import json
from .models import Person


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"Id": obj.id,
                "UserAddress": obj.UserAddress,
                "Password": obj.Password,
                "Email": obj.Email}


class NFTEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"NFTHash": obj.NFTHash,
                "NFTName": obj.NFTName,
                "NFTCost": obj.NFTCost}


class NFTAllEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"NFTOwner": obj.NFTOwner.UserAddress,
                "NFTHash": obj.NFTHash,
                "NFTName": obj.NFTName,
                "NFTCost": obj.NFTCost,
                }


class HistoryEncoder(json.JSONEncoder):
    def default(self, obj):
        return {
            "UserFrom": obj.UserAddressFrom.UserAddress,
            "UserTo": obj.UserAddressTo.UserAddress,
            "NFTName": obj.NFTInfo.NFTName,
            "NFTCost": obj.NFTInfo.NFTCost,
        }


