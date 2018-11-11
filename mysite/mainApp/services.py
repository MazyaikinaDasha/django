from .models import *
def create_card (question, answer, topic_id):
	card = Card(question,answer, topic_id)
	stat = Statistic(card.card_id)
def create_topic(name):
	topic=Topic(name)
def change_answer (card, value):
	card.answer=value
def change_question (card, value):
	card.question=value		
def show_summ_stat (stat):
	return stat.statistic_success + stat.statistic_unsuccess
def average_time(topic):
	return (topic.summ_time/topic.counter)
#def choose_by_knowledge(nomber):
	
def know(stat):
	stat.statistic_success+=1
def unknow(stat):
	stat.statistic_unsuccess+=1
				
