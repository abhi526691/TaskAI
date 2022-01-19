import csv
from email.mime import image
import logging
from unittest import result
from unittest.mock import patch
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import handle_uploaded_file, dest, data
from .forms import browse
import re
from django.urls import reverse
from django.contrib import messages
from datetime import datetime
from django.utils.dateparse import parse_date



def index(request):
	result = None
	form = None
	if request.method == 'POST':
		file = request.FILES['csv_file']
		dest.objects.create(
			file = file
		)
		handle_uploaded_file(request.FILES['csv_file'])
		path = 'static/upload/' + str(request.FILES['csv_file'])
		with open(path, 'rt') as f:
			data1 = csv.reader(f)
			for index, row in enumerate(data1):
				if index != 0:
					data.objects.create(
						image_name = row[0],
						object_detected = row[1],
						timestamp = parse_date(row[2])
					)		
		return HttpResponse("Thank you!!!")
	else:
		return render(request, 'index.html')


def data_show(request):
	if request.method == "POST":
		s_date = request.POST['s_date']
		e_date = request.POST['e_date']
		output_data = data.objects.filter(timestamp__range=(s_date, e_date))
		return render(request,'index.html', context={'zip_list' : output_data})
	else:
		return render(request, 'index.html')
		


