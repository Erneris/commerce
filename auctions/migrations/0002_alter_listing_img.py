# Generated by Django 3.2.9 on 2022-02-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]