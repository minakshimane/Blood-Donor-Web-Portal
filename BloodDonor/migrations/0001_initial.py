# Generated by Django 2.2.3 on 2020-06-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.IntegerField()),
                ('bloodgroup', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ldd', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('orgname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('orgtype', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StateCity',
            fields=[
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
