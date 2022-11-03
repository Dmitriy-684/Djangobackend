from django.db import models


class Person(models.Model):
    UserAddress = models.CharField(max_length=42, primary_key=True)
    Login = models.TextField()
    Password = models.TextField()


class NFTs(models.Model):
    NFTHash = models.CharField(max_length=46)


class History(models.Model):
    UserAddressFrom = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    UserAddressTo = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    TransferNFTHash = models.ForeignKey(NFTs, on_delete=models.DO_NOTHING)