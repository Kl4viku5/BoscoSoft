from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'ActivityEvaluation'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^evaluation/(?P<pk>[0-9]+)', views.EvaluationListView.as_view(), name='EvaluationList'),
    url(r'^evaluation_detail/(?P<pk>[0-9]+)', views.EvaluationDetail.as_view(), name='EvaluationDetail'),
    url(r'^activity_detail/(?P<pk>[0-9]+)', views.ActivityDetail.as_view(), name='activity_detail'),
]

urlpatterns += staticfiles_urlpatterns()