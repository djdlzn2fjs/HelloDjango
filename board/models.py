from django.db import models


# Create your models here.
from django.utils import timezone


class Board(models.Model):

    title = models.CharField(max_length=100)
    userid = models.CharField(max_length=18)
    regdate = models.DateTimeField(default=timezone.localtime)
    views = models.IntegerField(default=0)
    thumbup = models.IntegerField(default=0)
    contents = models.TextField()

class Employee(models.Model):

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hdate = models.DateField()
    jobid = models.CharField(max_length=20)
    salarys = models.IntegerField()
    commpct = models.FloatField()
    mgrid = models.IntegerField()
    deptid = models.IntegerField()

