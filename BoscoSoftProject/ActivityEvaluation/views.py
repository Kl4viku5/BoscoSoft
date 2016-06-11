from django.views import generic
from django.http import HttpResponseRedirect

from .models import Activity


class IndexView(generic.ListView):
    template_name = 'ActivityEvaluation/index.html'
    context_object_name = 'latest_activity_list'

    def get_queryset(self):
        return Activity.objects.order_by('name')[:100]


class ActivityDetailView(generic.DetailView):
    model = Activity
    template_name = 'ActivityEvaluation/activityDetail.html'
