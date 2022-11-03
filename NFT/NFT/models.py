from django.db import models


class Person():
    UserAddress = models.CharField(max_length=42, primary_key=True)
    Login = models.TextField()
    Password = models.TextField()


class NFTs():
    NFTHash = models.CharField(max_length=46)


class History():
    UserAddressFrom = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    UserAddressTo = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    TransferNFTHash = models.ForeignKey(NFTs, on_delete=models.DO_NOTHING)