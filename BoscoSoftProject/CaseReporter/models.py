import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Individual(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Case(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
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

