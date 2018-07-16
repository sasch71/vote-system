from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date =models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def getChoicesString(self):
        return "\n".join([c.__str__() for c in self.choicesrelated.all()])
    def getVoters(self):
        A=self.choicesrelated.first().getVoters()
        for c in self.choicesrelated.all() :
            A.union(c.getVoters(), all = False)
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
    isacurate = models.BooleanField(default= False)
    def __str__(self):
        return self.choice_text
    
    def addVoter(self,voter):
        self.voters=self.voters+ voter.__str__() +", "
    
    def getVotersString(self):
        return "\n".join([u.__str__() for u in self.votersID.all()])
    
    def getVoters(self):
        return self.votersID.all()
    
    def setAsAcurate(self):
        self.isacurate= True
        
        
    
    
def adjust(score, otherscore, result):
    k=100
    diff = otherscore - score
    f_factor = 1000
    return k*(result - 1. / (1 + 10 ** (diff / f_factor)))
    
def changeScore(question,acuratechoice):
    ratingW = 0
    ratingL = 0
    winners=acuratechoice.getVoters()
    loosers = question.getVoters().difference(winners)
    for w in winners:
        ratingW+= w.getScore()
    for l in loosers:
        ratingL += l.getScore()
    
        
        

    Win=adjust(ratingW, ratingL,1)
    Loose=adjust(ratingL,ratingW,0)
    
    for j in winners:
        j.modifyScore(j.getScore() + Win*ratingW/j.getScore())
        j.save()
            
    for i in loosers:
        i.modifyScore(i.getScore() + Loose*ratingL/i.getScore())
        i.save()
        
    return
        
        
    
    
    
