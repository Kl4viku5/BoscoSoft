from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'ActivityEvaluation'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^evaluation/(?P<pk>[0-9]+)', views.EvaluationListView.as_view(), name='EvaluationList'),
    url(r'^evaluation_detail/(?P<pk>[0-9]+)', views.EvaluationDetail.as_view(), name='evaluation_detail'),
    url(r'^activity_detail/(?P<pk>[0-9]+)', views.ActivityDetail.as_view(), name='activity_detail'),
    url(r'^evaluation_answer/new/(?P<question_pk>[0-9]+)', views.answer_new_with_question_id, name='evaluation_answers_new_with_question_id'),
    url(r'^evaluation_answer/new/$', views.answer_new, name='evaluation_answers_new'),
]

urlpatterns += staticfiles_urlpatterns()