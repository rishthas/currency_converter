# Generated by Django 2.1.4 on 2020-07-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200707_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profil_pic',
            field=models.CharField(max_length=100),
        ),
    ]
