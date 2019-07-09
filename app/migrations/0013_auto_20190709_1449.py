# Generated by Django 2.2.3 on 2019-07-09 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_attend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='attend',
            name='check_attend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Check_attend'),
        ),
    ]
