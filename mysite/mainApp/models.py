from django.db import models

# Create your models here.

class Statistic (models.Model):
    class Meta():
        db_table = "statictic"
    statistic_id = models.AutoField(primary_key=True)
    statistic_success = models.IntegerField(default=0)
    statistic_unsuccess = models.IntegerField(default=0)
    card_id = models.ForeignKey('Card',on_delete=models.CASCADE,)

    def __init__(self, card_id):
        self.statistic_unsuccess = 0
        self.statistic_success = 0
        self.card_id = card_id
    def __getattr__(self,name):
        return self.__dict__[name]
    def __setattr__(self, name, value):
        self.__dict__[name] = value    

class Card(models.Model):
    class Meta():
        db_table = "card"
    card_id = models.AutoField(primary_key=True)
    card_question = models.TextField(max_length=500)
    card_answer = models.TextField(max_length=500)
    topic_id = models.ForeignKey('Topic',on_delete=models.CASCADE,)

    def __init__(self,card_question, card_answer, topic_id):
        self.card_answer = card_answer
        self.card_question = card_question
        self.topic_id = topic_id
    def __getattr__(self,name):
        return self.__dict__[name]
    def __setattr__(self, name, value):
        self.__dict__[name] = value 
    def __del__(self):
        del self           

class Topic(models.Model):
    class Meta():
        db_table = "topic"
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=50)
    topic_time = models.TimeField(default=0)
    topic_dateView = models.DateField(default=0)
    topic_dateTest = models.DateField(default=0)
    
    summ_time = 0;
    counter = 0
    def __init__(topic_name):
        self.topic_name = topic_name
    def __getattr__(self,name):
        return self.__dict__[name]
    def __setattr__(self, name, value):
        self.__dict__[name] = value 
        if name == topic_time:
            counter+=1;
            summ_time+=value
    def __del__(self):
        del self            








