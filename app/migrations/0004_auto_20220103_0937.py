# Generated by Django 3.0.5 on 2022-01-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211231_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='eventCoOrdinator2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='eventCoOrdinator2Mob',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
