from django.contrib.auth.models import AbstractUser
from django.db import models
from polls.models import Choice

class CustomUser(AbstractUser):
    # add additional fields in here
    
    score=models.FloatField(default=1000)
    choices=models.ManyToManyField(Choice,related_name='votersID')

    def __str__(self):
        return self.username
    
    def getChoices(self):
        return "\n".join([c.__str__() for c in self.choices.all()])
    
    def getScore(self):
        return self.score
    
    def modifyScore(self, newvalue):
        self.score=newvalue
        return
    
    def addChoice(self, choice):
        self.choices.add(choice)