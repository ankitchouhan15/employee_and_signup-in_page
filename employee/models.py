from django.db import models

# Create your models here.


class employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=25, unique=True)
    mobile = models.CharField(max_length=12, unique=True)
    salary = models.FloatField()
    city = models.CharField(max_length=25)


class Meta:
    db_table = "empdata"
