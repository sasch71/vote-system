from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.conf import settings


from .models import Choice, Question
from django.template import loader



#class IndexView(generic.ListView):
#    template_name = 'polls/index.html'
#    context_object_name = 'latest_question_list'
#
#    def get_queryset(self):
#        return Question.objects.order_by('-pub_date')[:]


def index(request):
    latest_question_list = Question.objects.none()
    if request.user.isPartner:
        latest_question_list = latest_question_list.union(Question.objects.filter(ispartner=True))
    if request.user.isPartner2:
        latest_question_list = latest_question_list.union(Question.objects.filter(ispartner2=True))
    if request.user.isSeniorDirector:
        latest_question_list = latest_question_list.union(Question.objects.filter(isseniordirector=True))
    if request.user.isManager:
        latest_question_list = latest_question_list.union(Question.objects.filter(ismanager=True))
    if request.user.isAdmin:
        latest_question_list = latest_question_list.union(Question.objects.filter(isadmin=True))
    if request.user.isStaff:
        latest_question_list = latest_question_list.union(Question.objects.filter(isstaff=True))
   
        
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list.order_by('-pub_date')[:],
    }
    return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    theme=question.theme
    adminvoted = request.POST.get('adminvote',False)
    try:
        selected_choice = question.choicesrelated.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })


    
    else:
        
        if adminvoted:
            selected_choice.setAsAcurate()
            selected_choice.save()
            question.changeScore()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
        if not question.getVoters().filter(id=request.user.id):
            selected_choice.votes += request.user.getScore(theme)
            selected_choice.addVoter(request.user)
            request.user.addChoice(selected_choice)
            selected_choice.save()
        else:
            return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You already voted",
             })
        
    
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

