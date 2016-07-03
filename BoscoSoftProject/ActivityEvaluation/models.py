import datetime

from django.db import models
from django.utils import timezone


class Activity(models.Model):
    """
    Activity represent an event that took place wich is then going to
    be rated using an EvaluationGrid.
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField('Date de début')
    end_date = models.DateTimeField('Date de fin')

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    """
    Evaluation represent the overall rating of the activity.
    There can be more than one evaluation for an activity.
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        name = "Évaluation de l'activité : "
        name += self.activity.name
        return name

    # Return true if case was published during the last 5 days
    def was_published_recently(self):
        now = timezone.now()
        delta = datetime.timedelta(days=5)
        return now - delta <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publié récemment'


class Question(models.Model):
    """
    Question represents the question to wich the user will have to reply
    to during the evaluation.
    """
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description


class Answer(models.Model):
    """
    An answer is linked to a question, there can be more than one answer.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    explanation = models.CharField(max_length=1000)
    CHOICES = (
        (0, "Fortement en désaccord"),
        (1, "Plutôt en désaccord"),
        (2, "Sans opinion"),
        (3, "Plutôt d’accord"),
        (4, "Fortement d’accord"),
    )

