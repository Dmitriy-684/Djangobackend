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


class HistoryEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"Id": obj.id,
                "UserAdressFrom": obj.UserAddressFrom,
                "UserAddressTo": obj.UserAddressTo,
                "NFTInfo": obj.NFTInfo}

