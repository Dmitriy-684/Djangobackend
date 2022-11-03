import json
from .models import Person


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"Id": obj.id,
                "UserAddress": obj.UserAddress,
                "Login": obj.Login,
                "Password": obj.Password}


class NFTEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"Id": obj.id,
                "NFTHash": obj.NFTHash}


class History(json.JSONEncoder):
    def default(self, obj):
        return {"Id": obj.id,
                "UserAdressFrom": obj.UserAddressFrom,
                "UserAddressTo": obj.UserAddressTo,
                "TransferNFTHash": obj.TransferNFTHash}


class AllPerson(json.JSONEncoder):
    def default(self, obj):
        result = dict()
        for person in obj:
            result[person.id] = {"Id": person.id,
                                 "UserAddress": person.UserAddress,
                                 "Login": person.Login,
                                 "Password": person.Password}
        return result

