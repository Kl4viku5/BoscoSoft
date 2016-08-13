from django.views import generic
from django.shortcuts import render, redirect

from .models import Activity, Evaluation, Answer, Question
from .forms import AnswerForm


def answer_new(request):
    form = AnswerForm()
    return render(request, 'ActivityEvaluation/answer_new.html', {'form': form})


def answer_new_with_question_id(request, question_pk):
    form = AnswerForm()
    question = Question.objects.get(pk=question_pk)
    answer = Answer(question=question)
    return render(request, 'ActivityEvaluation/answer_new.html', {'form': form, 'answer': answer})


class EvaluationListView(generic.ListView):
    template_name = 'ActivityEvaluation/evaluation_list.html'
    context_object_name = 'latest_evaluation_list'

    def get_queryset(self):
        return Evaluation.objects.filter(request).order_by('pub_date')[:100]


class EvaluationDetail(generic.DetailView):
    template_name = 'ActivityEvaluation/evaluation_detail.html'
    model = Evaluation

    def post(self, request, *args, **kwargs):
        evaluationid = request.POST['evaluationid']
        questions = Question.objects.filter(evaluation=evaluationid)
        for question in questions:
            value = request.POST['question' + str(question.id)]
            answer = Answer(question=question, explanation="asdasfasdasd", score=value)
            answer.save()
        return redirect('/ActivityEvaluation')


class EvaluationCreate(generic.CreateView):
    template_name = 'ActivityEvaluation/evaluation_form.html'
    model = Evaluation
    fields = ['description']


class ActivityListView(generic.ListView):
    template_name = 'ActivityEvaluation/activity_list.html'
    context_object_name = 'latest_activity_list'

    def get_queryset(self):
        return Activity.objects.order_by('name')[:100]


class ActivityDetail(generic.DetailView):
    template_name = 'ActivityEvaluation/activity_detail.html'
    model = Activity


class ActivityCreate(generic.CreateView):
    template_name = 'ActivityEvaluation/activity_form.html'
    model = Activity
    fields = ['name', 'description', 'start_date', 'end_date']

    def get_form(self):
        form = super(ActivityCreate, self).get_form()
        form.fields['start_date'].widget.attrs.update({'class': 'datepicker'})
        form.fields['end_date'].widget.attrs.update({'class': 'datepicker'})
        return form


class ActivityUpdate(generic.UpdateView):
    template_name = 'ActivityEvaluation/activity_update_form.html'
    model = Activity
    fields = ['name', 'description', 'start_date', 'end_date']

    def get_form(self):
        form = super(ActivityUpdate, self).get_form()
        form.fields['start_date'].widget.attrs.update({'class': 'datepicker'})
        form.fields['end_date'].widget.attrs.update({'class': 'datepicker'})
        return form


class ActivityDelete(generic.DeleteView):
    model = Activity
    success_url = '/ActivityEvaluation'