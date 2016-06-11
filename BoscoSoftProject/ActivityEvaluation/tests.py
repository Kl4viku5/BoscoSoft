import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Evaluation

# Tests were inspired by Django polls tutorial
# https://docs.djangoproject.com/en/1.9/intro/


def create_evaluation(days=None, hours=None):
    if days is None:
        time = timezone.now() + datetime.timedelta(hours=hours)
        return Evaluation(pub_date=time)
    else:
        time = timezone.now() + datetime.timedelta(days=days)
        return Evaluation(pub_date=time)


class EvaluationMethodTests(TestCase):

    def test_was_published_recently_with_future_evaluation(self):
        future_evaluation = create_evaluation(days=30)
        self.assertEqual(future_evaluation.was_published_recently(), False)

    def test_was_published_recently_with_old_evaluation(self):
        old_evaluation = create_evaluation(days=-30)
        self.assertEqual(old_evaluation.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_evaluation = create_evaluation(hours=-1)
        self.assertEqual(recent_evaluation.was_published_recently(), True)