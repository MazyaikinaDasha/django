from django.db import models

# Create your models here.

class Statistic (models.Model):
    class Meta():
        db_table = "statictic"
    id = models.AutoField(primary_key=True)
    success = models.IntegerField(default=0)
    unsuccess = models.IntegerField(default=0)
    card_id = models.ForeignKey('Card',on_delete=models.CASCADE,)

    def __init__(self, card_id):
        self.unsuccess = 0
        self.success = 0
        self.card_id = card_id
    def __getattr__(self,name):
        return self.__dict__[name]
    def __setattr__(self, name, value):
        self.__dict__[name] = value    

class Card(models.Model):
    class Meta():
        db_table = "card"
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    top = models.ForeignKey('Topic',on_delete=models.CASCADE,)


    def __str__(self):
        return self.question



    def __del__(self):
        del self           

class Topic(models.Model):
    class Meta():
        db_table = "topic"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    time = models.TimeField(default=0)
    dateView = models.DateField(default=0)
    dateTest = models.DateField(default=0)
    
    summ_time = 0
    counter = 0
    def __init__(self,name):
        self.name = name
    def __getattr__(self,name):
        return self.__dict__[name]
    def __setattr__(self, name, value):
        self.__dict__[name] = value 
        if name == self.topic_time:
            self.counter+=1;
            self.summ_time+=value
    def __del__(self):
        del self            







