from django.views import generic

from .models import Activity, Evaluation


class IndexView(generic.ListView):
    template_name = 'ActivityEvaluation/index.html'
    context_object_name = 'latest_activity_list'

    def get_queryset(self):
        return Activity.objects.order_by('name')[:100]


class EvaluationListView(generic.ListView):
    template_name = 'ActivityEvaluation/EvaluationList.html'
    context_object_name = 'latest_evaluation_list'

    def get_queryset(self):
        return Evaluation.objects.filter(request).order_by('pub_date')[:100]


class EvaluationDetail(generic.DetailView):
    template_name = 'ActivityEvaluation/EvaluationDetail.html'
    model = Evaluation


class ActivityDetail(generic.DetailView):
    template_name = 'ActivityEvaluation/activity_detail.html'
    model = Activity
