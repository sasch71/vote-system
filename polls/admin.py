from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Register your models here.
from .models import Question, Choice


from django.contrib.admin.views.decorators import staff_member_required


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['question_text', 'getChoicesString', 'theme']
   


  
    
class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ['question','choice_text', 'votes', 'getVotersString']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)