from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Register your models here.
from .models import Question, Choice
from users.models import CustomUser
from django.core.mail import send_mail

from django.contrib.admin.views.decorators import staff_member_required


def sendmail(modeladmin, request, queryset):
    for q in queryset:
        user_list = CustomUser.objects.none()
        if q.ispartner:
            user_list = user_list.union(CustomUser.objects.filter(isPartner=True))
        if q.ispartner2:
            user_list = user_list.union(CustomUser.objects.filter(isPartner2=True))
        if q.isseniordirector:
            user_list = user_list.union(CustomUser.objects.filter(isSeniorDirector=True))
        if q.ismanager:
            user_list = user_list.union(CustomUser.objects.filter(isManager=True))    
        if q.isadmin:
            user_list = user_list.union(CustomUser.objects.filter(isAdmin=True))
        if q.isstaff:
            user_list = user_list.union(CustomUser.objects.filter(isStaff=True))
        send_mail('New poll', 'There is a new poll you can answer : %s' %(q.question_text,   ) , [user_list.values_list('email', flat=True)])
sendmail.short_description = 'Send mail to concerned users'
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['question_text', 'getChoicesString', 'theme']
    actions= [sendmail]
   


  
    
class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ['question','choice_text', 'votes', 'getVotersString']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)