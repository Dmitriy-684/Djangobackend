from django.db import models


class Person(models.Model):
    UserAddress = models.CharField(max_length=42, unique=True, verbose_name="Адрес кошелька пользователя")
    Password = models.TextField(verbose_name="Пароль пользователя")
    Email = models.CharField(max_length=256, unique=True, verbose_name="Адрес почты пользователя")


class NFTs(models.Model):
    NFTHash = models.CharField(max_length=46, verbose_name="Хэш код HFT")
    NFTOwner = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="Owner", verbose_name="Владелец")


class History(models.Model):
    UserAddressFrom = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="UserFrom", verbose_name="Продавец")
    UserAddressTo = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="UserTo", verbose_name="Покупатель")
    TransferNFTHash = models.ForeignKey(NFTs, on_delete=models.DO_NOTHING, verbose_name="Продаваемая API")
    Cost = models.FloatField(verbose_name="Цена", default=0)

