# Generated by Django 2.2.3 on 2019-07-09 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_attend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='part',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.Part', verbose_name='所属'),
        ),
    ]
