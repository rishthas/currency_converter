# Generated by Django 3.0.8 on 2020-07-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200707_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='room_no',
            field=models.CharField(max_length=10),
        ),
    ]
