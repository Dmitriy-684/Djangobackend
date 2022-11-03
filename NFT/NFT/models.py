from django.db import models


class Person(models.Model):
    UserAddress = models.CharField(max_length=42, primary_key=True, verbose_name="Адрес кошелька пользователя")
    Login = models.TextField(verbose_name="Логин пользователя")
    Password = models.TextField(verbose_name="Пароль пользователя")

    def __str__(self):
        return self.Login


class NFTs(models.Model):
    NFTHash = models.CharField(max_length=46, verbose_name="Хэш код NFT")

    def __str__(self):
        return self.NFTHash

class History(models.Model):
    UserAddressFrom = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="UserFrom", verbose_name="Продавец")
    UserAddressTo = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="UserTo", verbose_name="Покупатель")
    TransferNFTHash = models.ForeignKey(NFTs, on_delete=models.DO_NOTHING, verbose_name="Продаваемая NFT")

    def __str__(self):
        return f"From: {self.UserAddressFrom} --- To: {self.UserAddressTo}"

