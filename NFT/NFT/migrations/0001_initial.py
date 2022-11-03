# Generated by Django 4.1.3 on 2022-11-03 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFTs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NFTHash', models.CharField(max_length=46, verbose_name='Хэш код NFT')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('UserAddress', models.CharField(max_length=42, primary_key=True, serialize=False, verbose_name='Адрес кошелька пользователя')),
                ('Login', models.TextField(verbose_name='Логин пользователя')),
                ('Password', models.TextField(verbose_name='Пароль пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransferNFTHash', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='NFT.nfts', verbose_name='Продаваемая NFT')),
                ('UserAddressFrom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='UserFrom', to='NFT.person', verbose_name='Продавец')),
                ('UserAddressTo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='UserTo', to='NFT.person', verbose_name='Покупатель')),
            ],
        ),
    ]
