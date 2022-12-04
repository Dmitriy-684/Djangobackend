from django.db import models


class Person(models.Model):
    UserAddress = models.CharField(max_length=42, unique=True, verbose_name="Адрес кошелька пользователя")
    Password = models.TextField(verbose_name="Пароль пользователя")
    Email = models.CharField(max_length=256, unique=True, verbose_name="Адрес почты пользователя")


class Nft(models.Model):
    NFTHash = models.CharField(max_length=46, verbose_name="Хэш код NFT", unique=True)
    NFTOwner = models.ForeignKey(Person, db_column='UserAddress', on_delete=models.DO_NOTHING, related_name="Owner", verbose_name="Владелец")
    NFTCost = models.FloatField(verbose_name="Цена", default=0)
    NFTName = models.CharField(max_length=31, verbose_name="Имя картинки")


class History(models.Model):
    UserAddressFrom = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="UserFrom", verbose_name="Продавец")
    UserAddressTo = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="UserTo", verbose_name="Покупатель")
    NFTInfo = models.ForeignKey(Nft, on_delete=models.DO_NOTHING, verbose_name="Продаваемая NFT")
