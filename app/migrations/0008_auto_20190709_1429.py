# Generated by Django 2.2.3 on 2019-07-09 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190709_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]