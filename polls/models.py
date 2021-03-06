from django.db import models
from django.contrib.auth.models import Group



# Create your models here.
class Question(models.Model):
    THEMES_POSSIBLES = (
        ('General', 'General'),
        ('Business', 'Business'),
        ('Development', 'Development'),
        ('Operation', 'Operations'),
        ('Strategy', 'Strategy'),
        ('Techno', 'Techno'),
        ('Management', 'Management'))
    
    
    question_text = models.CharField(max_length=200)
    pub_date =models.DateTimeField('date published')
    theme= models.CharField(max_length=200, choices = THEMES_POSSIBLES, default='General')
    
    """target groups"""
    ispartner=models.BooleanField(default=True, verbose_name='For Partners')
    ispartner2=models.BooleanField(default=True, verbose_name='For Partners 2')
    isseniordirector=models.BooleanField(default=True, verbose_name='For Senior Directors')
    ismanager=models.BooleanField(default=True, verbose_name='For Managers')
    isadmin=models.BooleanField(default=True, verbose_name='For Admins')
    isstaff=models.BooleanField(default=True, verbose_name='For Staff')
    
    
    def __str__(self):
        return self.question_text
    def getChoicesString(self):
        return "\n".join([c.__str__() for c in self.choicesrelated.all()])
    getChoicesString.short_description= 'Choices'
    
    def getVoters(self):
        A=self.choicesrelated.first().getVoters()
        for c in self.choicesrelated.all() :
            if c.getVoters():
                A=A.union(c.getVoters(), all = False)
        return A
    def hasVoted(self,userid):
        A=self.choicesrelated.first().getVoters().filter(id=userid)
        for c in self.choicesrelated.all() :
            if c.getVoters():
                A=A.union(c.getVoters().filter(id=userid), all = False)
        return A
    
    def getAcurateChoice(self):
        return self.choicesrelated.get(isacurate = True)
    
    def changeScore(self):
        changeScore(self, self.getAcurateChoice())
    
class Choice(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choicesrelated')
    choice_text = models.CharField(max_length=200)
    votes = models.FloatField(default=0)
    voters = models.CharField(max_length=4000, default='', blank=True)
    isacurate = models.BooleanField(default= False, verbose_name='Is the acurate answer')
    def __str__(self):
        return self.choice_text
    
    def addVoter(self,voter):
        self.voters=self.voters+ voter.__str__() +", "
        self.save()
        
    def getVotersString(self):
        return "\n".join([u.__str__() for u in self.votersID.all()])
    getVotersString.short_description='Who voted'
    def getVoters(self):
        return self.votersID.all()
    
    def setAsAcurate(self):
        self.isacurate= True
        self.save()
        

       
    
    
def adjust(score, otherscore, result):
    k=50
    diff = otherscore - score
    f_factor = 1000
    return k*(result - 1. / (1 + 10 ** (diff / f_factor)))
    
def changeScore(question,acuratechoice):
    theme=question.theme
    ratingW = 0
    ratingL = 0
    winners = acuratechoice.getVoters()
    print(winners)
    loosers = question.getVoters().difference(winners)
    print(loosers)
    for w in winners:
        ratingW += w.getScore(theme)
    for l in loosers:
        ratingL += l.getScore(theme)
        
    print(ratingW)
    print(ratingL)
    
        
        

    Win=adjust(ratingW, ratingL,1)
    Loose=adjust(ratingL,ratingW,0)
    print(Win)
    print(Loose)
    for j in winners:
        j.modifyScore(max(j.getScore(theme) + Win*max(ratingW,ratingL)/j.getScore(theme), 300),theme)
        j.save()
            
    for i in loosers:
        i.modifyScore(max(i.getScore(theme) + Loose*ratingL/i.getScore(theme), 300),theme)
        i.save()
        
        
        
    
    
    
