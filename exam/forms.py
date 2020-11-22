from .models import Exam, Pattern
from django.forms import ModelForm
from inspect import signature




class Exam_Form(ModelForm):
	
	class Meta:
		model = Exam
		fields = ['name']

class Exam_pattern(ModelForm):
	class Meta:
		model = Pattern
		fields = ['name','exam']





