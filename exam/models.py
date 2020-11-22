from django.db import models


# Create your models here.

class Exam(models.Model):
	name = models.CharField(max_length=90, null=True)
	Published_date = models.DateTimeField(auto_now_add=True)
	

class Pattern(models.Model):
	name = models.CharField(max_length=30) 
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

class Question(models.Model):
	name=models.CharField(max_length=10)	
	content= models.TextField()
	answer = models.CharField(max_length=100)
	pattern = models.ManyToManyField(Pattern)
	exam = models.ManyToManyField(Exam)

class Option(models.Model):
	name=models.CharField(max_length=5)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)






