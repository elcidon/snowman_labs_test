# Generated by Django 2.2.9 on 2020-09-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0006_auto_20200926_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='latitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='spot',
            name='longitude',
            field=models.CharField(max_length=50),
        ),
    ]