from django.contrib.auth.models import AbstractUser
from django.db import models
from polls.models import Choice
from jsonfield import JSONField


class CustomUser(AbstractUser):
    # add additional fields in here
    """groups"""
    isPartner=models.BooleanField(default=False)
    isPartner2=models.BooleanField(default=False)
    isSeniorDirector=models.BooleanField(default=False)
    isManager=models.BooleanField(default=False)
    isAdmin=models.BooleanField(default=False)
    isStaff=models.BooleanField(default=True)
    
    """scores"""
    score=models.FloatField(default=1000)
    scoreBus=models.FloatField(default=1000)
    scoreDev=models.FloatField(default=1000)
    scoreTech=models.FloatField(default=1000)
    scoreStrat=models.FloatField(default=1000)
    scoreManag=models.FloatField(default=1000)
    scoreOp=models.FloatField(default=1000)
    
    
    choices=models.ManyToManyField(Choice,related_name='votersID')  
    
    
    def getScore(self, theme):
        scores={ 'General': self.score,
                'Business': self.scoreBus,
                'Developement': self.scoreDev,
                'Tech': self.scoreTech,
                'Strategy': self.scoreStrat,
                'Management': self.scoreManag,
                'Operations': self.scoreOp}
        return scores[theme]
    


    def __str__(self):
        return self.username
    
    def getChoices(self):
        return "\n".join([c.__str__() for c in self.choices.all()])
    
    
    def modifyScoreGen(self, newvalue):
        self.score=newvalue
        return
    def modifyScoreBus(self, newvalue):
        self.scoreBus=newvalue
        return
    def modifyScoreDev(self, newvalue):
        self.scoreDev=newvalue
        return
    def modifyScoreTech(self, newvalue):
        self.scoreTech=newvalue
        return
    def modifyScoreStrat(self, newvalue):
        self.scoreStrat=newvalue
        return
    def modifyScoreManag(self, newvalue):
        self.scoreManag=newvalue
        return
    def modifyScoreOp(self, newvalue):
        self.scoreOp=newvalue
        return
    def addChoice(self, choice):
        self.choices.add(choice)
    
    def modifyScore(self, theme, newvalue):
        if theme=='General':
            self.modifyScoreGen(newvalue)
        elif theme=='Development':
            self.modifyScoreDev(newvalue)
        elif theme=='Business':
            self.modifyScoreBus(newvalue)
        elif theme=='Tech':
            self.modifyScoreTech(newvalue)
        elif theme=='Strategy':
            self.modifyScoreStrat(newvalue)
        elif theme=='Management':
            self.modifyScoreManag(newvalue)
        elif theme=='Operations':
            self.modifyScoreOp(newvalue)
        
