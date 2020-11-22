from django.shortcuts import render
from exam.forms import *
from django.http import HttpResponse
from django.shortcuts import render,redirect
from exam.models import *
from django.contrib import messages
import inspect as ins
from pprint import pprint

def obj_inspect():
	pass


def home(request):
	q_form= Exam_Form()
	exam_names_list = Exam.objects.all()
	if request.method=='GET':

		if request.path=='/home/':
		
			if request.GET:
				
				q_form=Exam_Form(request.GET)
				if q_form.is_valid():
				
					exam=Exam(name=q_form.cleaned_data['name'])
					exam.save()

					messages.info(request,'Exam name added!')
					context = {'form': q_form,'e_name':exam_names_list}
					return render(request,'home.html',context)

		elif request.path=='/delete/':
			exam=Exam.objects.all()
			if exam:
				exam.last().delete()
			else:
				messages.info(request,'No Exam names to delete!')
				
				context = {'form': q_form,'e_name':exam_names_list}
				return render(request,'home.html',context)

		else:
			print(dir(request))
			print(request.path)
			
			context = {'form': q_form,'e_name':exam_names_list}
			return render(request,'home.html',context)
	
	context = {'form': q_form,'e_name':exam_names_list}
	return render(request,'home.html',context)
a=0
def info(request):
	global a

	messages.success(request,f'Success is at  view info {a}')
	a+=1
	print(a)
	# from inspect import signature
	# sig=signature(redirect)
	# print(dir(redirect))
	# print(sig,sig.parameters)
	# return render(request,'info.html')
	return redirect('/check')

def check(request):
	# global a
	
	
	return render(request,'templates/exam/base.html')