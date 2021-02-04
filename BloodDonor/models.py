from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)

class Donor(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    bloodgroup = models.CharField(max_length=5)
    country=models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    ldd = models.DateField()

class Organisation(models.Model):
    Orgid=models.IntegerField(unique=True,null=True)
    orgname = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    orgtype = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address=models.CharField(max_length=50,null=True)
    contact = models.IntegerField()

class StateCity(models.Model):
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30,primary_key=True)

class Inbox(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    email=models.EmailField(max_length=30,null=True)
    contact=models.IntegerField(null=True)
    message = models.CharField(max_length=150)


