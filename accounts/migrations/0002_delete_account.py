# Generated by Django 2.2.10 on 2020-09-29 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0002_auto_20200929_1418'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]