# Generated by Django 2.2.3 on 2019-07-09 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Part'),
            preserve_default=False,
        ),
    ]