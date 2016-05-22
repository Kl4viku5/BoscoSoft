from django.views import generic
from django.utils import timezone

from .models import Individual


class IndexView(generic.ListView):
    template_name = 'CaseReporter/index.html'
    context_object_name = 'latest_individual_list'

    def get_queryset(self):
        return Individual.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
    model = Individual
    template_name = 'CaseReporter/detail.html'