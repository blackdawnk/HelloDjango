from django.db import models
from django.utils import timezone

class Board(models.Model):
    # id = models.IntegerField()   # id는 자동생성이므로 생략 가능
    title = models.CharField(max_length=100)
    userid = models.CharField(max_length=18)
    regdate = models.DateTimeField(default=timezone.localtime)
    views = models.IntegerField(default=0)
    contents = models.TextField()
    thumbup = models.IntegerField(default=0)

class Employees(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    hdate = models.DateField()
    jobid = models.CharField(max_length=255)
    sal = models.IntegerField()
    comm = models.FloatField()
    mgrid = models.IntegerField()
    deptid = models.IntegerField()

