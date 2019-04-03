from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.template import loader
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from . import forms


def welcome(request):
    return render(request, 'first_app/index.html', {})

#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'first_app/index.html', context)
#
#
#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def detail(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'detail.html', {'question': question})
#
#
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'results.html', {'question': question})
#
#
# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'results.html'
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNOtExist):
#         return render(request, 'first_app/detail.html', {
#                                'question': question,
#                                 'error_massage': "You did not select a choice."
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('first_app:results', args=(question_id,)))
#
#
# @csrf_exempt
# def test(request):
#
#     age = request.POST['age']
#     return JsonResponse({'age': age}, JSONEncoder)


# def form_view(request):
#     form = forms.MyForm()
#     if request.method == 'POST':
#         form = forms.MyForm(request.POST)
#         if form.is_valid():
#             # print(request.POST)
#             print("validation success")
#             print("Name :" + form.cleaned_data['name'])
#             print("Email :" + form.cleaned_data['email'])
#             print("Text :" + form.cleaned_data['text'])
#
#     return render(request, 'first_app/form_page.html', context={'form': form})


def user_view(request):

    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return welcome(request)
    else:
        print("Error, form is invalid")

    return render(request, 'first_app/form_page.html', context={'form': form})
