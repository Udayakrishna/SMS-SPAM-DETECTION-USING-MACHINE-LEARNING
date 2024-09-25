
from django.shortcuts import render

from .models import predict
from django.shortcuts import render
import requests
import numpy as np
import pandas as pd
import pickle

from django.http import HttpResponse
def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)
    #print(lines_list)
    return lines_list


# Create your views here.
def home(request):
	return render(request,'login.html')
def again(request):
	return render(request,'login.html')

def input(request):
    file_name = 'account.txt'
    name = request.POST.get('name')
    password = request.POST.get('password')
    account_list = read_file(file_name)
    print(name)
    print(password)
    for i in account_list:

        if i[0] == name  and i[1] == password:
            print(i[0])
            print(i[1])
            return render(request,'index.html')
        else:
            return HttpResponse('Wrong Password or Name', content_type='text/plain')
def input1(request):
	return render(request,'index.html')

def output(request):
	algo = request.POST.get('algo')
	text = [str(request.POST.get('text'))]
	out=predict(text,algo)
	#classes = class_names[int(out)]
	print('Ouptput:-',out)
	if out == 1:
		class_name = 'sms detected as SPAM kindly avoid'
	else:
		class_name = 'HEY HI.. 1 message recived'
	print(class_name)
	return render(request,'output.html',{'out':class_name})