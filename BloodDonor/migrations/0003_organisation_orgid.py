# Generated by Django 2.2.3 on 2020-07-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodDonor', '0002_auto_20200705_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='Orgid',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
