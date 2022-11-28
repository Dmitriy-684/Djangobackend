# Generated by Django 4.1.3 on 2022-11-23 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0014_alter_nft_nftowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='NFTOwner',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='Owner', to='API.person', verbose_name='Владелец'),
        ),
    ]
