from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['question_text', 'getChoicesString']
    
class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ['question','choice_text', 'votes', 'getVotersString']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)