import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

#Represent an Activity


class Activity(models.Model):
    """
    Activity represent an event that took place wich is then going to
    be rated using an EvaluationGrid.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    """
    Evaluation represent the overall rating of the activity.
    There can be more than one evaluation for an activity.
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    # Return true if case was published during the last 5 days
    def was_published_recently(self):
        now = timezone.now
        delta = datetime.timedelta(days=5)
        return now - delta <= self.pubdate <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publié récemment'


class Subject(models.Model):
    """
    Subject represents the question to wich the user will have to reply
    to during the evaluation.
    """
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description


