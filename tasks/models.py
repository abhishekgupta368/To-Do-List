from django.db import models
from datetime import datetime
import pytz

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=100, blank=False)
    due_date = models.DateTimeField(blank=False)
    catorgery = [
        ('0','Other'),
        ('1','Shopping'),
        ('2','Work '),
        ('3','Personal'),
        ('4','Grocery'),
        ('5','Assignment')
    ]
    user_choice  = models.CharField(max_length=50,choices=catorgery,default='0',blank=False)

    def __str__(self):
        return self.title
    
    def deadline_reached(self):
        utc=pytz.UTC
        return utc.localize(datetime.now()) < self.due_date

# class User(models.Model):
#     name = models.CharField(max_length=50, blank=False)
#     email = models.CharField(max_length=50, blank=False)
#     password = models.CharField(max_length=50, blank=False)

#     def __str__(self):
#         return self.email