# Generated by Django 4.1.3 on 2022-11-28 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0018_remove_history_cost_remove_history_transfernfthash_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="NftInfo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="info",
                to="API.nft",
                verbose_name="Информация",
            ),
        ),
        migrations.AlterField(
            model_name="history",
            name="UserAddressFrom",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="UserFrom",
                to="API.person",
                verbose_name="Продавец",
            ),
        ),
        migrations.AlterField(
            model_name="history",
            name="UserAddressTo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="UserTo",
                to="API.person",
                verbose_name="Покупатель",
            ),
        ),
    ]
