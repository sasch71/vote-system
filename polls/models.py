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
            A.union(c.getVoters())
        return A
    
class Choice(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choicesrelated')
    choice_text = models.CharField(max_length=200)
    votes = models.FloatField(default=0)
    voters = models.CharField(max_length=4000, default='', blank=True)
    def __str__(self):
        return self.choice_text
    
    def addVoter(self,voter):
        self.voters=self.voters+ voter.__str__() +", "
    
    def getVotersString(self):
        return "\n".join([u.__str__() for u in self.votersID.all()])
    
    def getVoters(self):
        return self.votersID.all()
    
    
    

    