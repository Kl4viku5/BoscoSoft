from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'ActivityEvaluation'
urlpatterns = [
    url(r'^$',
        views.ActivityListView.as_view(),
        name='activity_list'),

    url(r'^evaluation/(?P<pk>[0-9]+)',
        views.EvaluationListView.as_view(),
        name='evaluation_list'),

    url(r'^evaluation_detail/(?P<pk>[0-9]+)',
        views.EvaluationDetail.as_view(),
        name='evaluation_detail'),

    url(r'^activity_detail/(?P<pk>[0-9]+)',
        views.ActivityDetail.as_view(),
        name='activity_detail'),

    url(r'^evaluation_answer/new/(?P<question_pk>[0-9]+)',
        views.answer_new_with_question_id,
        name='evaluation_answers_new_with_question_id'),

    url(r'^evaluation_answer/new/$',
        views.answer_new,
        name='evaluation_answers_new'),

    url(r'^evaluation_create/(?P<activity_pk>[0-9]+)',
        views.EvaluationCreate.as_view(),
        name='evaluation_form'),

    url(r'^activity_creation$',
        views.ActivityCreate.as_view(success_url='/ActivityEvaluation'),
        name='activity_form'),

    url(r'^activity_update/(?P<pk>[0-9]+)$',
        views.ActivityUpdate.as_view(success_url='/ActivityEvaluation'),
        name='activity_update_form'),

    url(r'^activity_delete/(?P<pk>[0-9]+)$',
        views.ActivityDelete.as_view(),
        name='activity_confirm_delete'),
]

urlpatterns += staticfiles_urlpatterns()