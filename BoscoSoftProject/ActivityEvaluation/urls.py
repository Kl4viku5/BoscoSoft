from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'ActivityEvaluation'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)', views.DetailView.as_view(), name='detail'),
]

urlpatterns += staticfiles_urlpatterns()