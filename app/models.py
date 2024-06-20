from django.db import models

# Create your models here.

class team_ceac_activities(models.Model):
    target = models.CharField(max_length=200)
    on_going = models.CharField(max_length=200)
    completed = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)
    guideline_activity = models.CharField(max_length=200)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)

    def __str__(self):
        return self.status
