from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect

import requests
import tempfile
import re
from lxml import html
import csv

from requests.auth import HTTPBasicAuth
from report.models import *


def home(request):
	lista1=[]
	a=request.POST.get('iTravel', '---')
	lista1.append(a)
	
	h_list=compute(lista1)
	
	template = loader.get_template('report/home.html')
	context = RequestContext(request, {
		'h_list': h_list,
		})
	return HttpResponse(template.render(context))


def full(request):
	
	town= request.POST.get('town', '---')  
	lista2=[]
	if town=="thermi":
		lista2=[21,22,23,24]
	elif town=="agios":
		lista2=[25,26,27,28,29,30]
	elif town=="serres":
		lista2=[56,57,58,59]
	elif town=="kavala":
		lista2=[60,61,62,63]
	elif town=="patra":
		lista2=[64,65,66,67,68,69,70,71]
	elif town=="chalkidiki":
		lista2=[77,78,79,80,81,82]
	elif town=="kalamata":
		lista2=[200,201,202]
	elif town=="all":
		lista2=[] #25,26,27,28,29,30,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,78,79,80,81,82,200,201,202]


	full_list=compute(lista2)
	
	template = loader.get_template('report/full.html')
	context = RequestContext(request, {
		'full_list': full_list,
		})
	return HttpResponse(template.render(context))



def compute(lista):
	iTravel_list=[]
	bluetooth_logger=[]
	bluetooth_status=[]
	system_time=[]
	wan_status=[]
	sdcard_status=[]
	for iTravel in lista: # [25,26,27,28,29,30,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,78,79,80,81,82,200,201,202]:
		iTravel_list.append(iTravel)

		try:
			s = requests.Session()
			r=s.get('http://xxxxxxx'+str(iTravel)+'xxxxxxx', auth=HTTPBasicAuth('xxxxxxx', 'xxxxxxx'))				
			tree = html.fromstring(r.text)		
			bluetooth_logger.append(tree.xpath('//span[@id="bt-logger-status"] //font /text()'))
			system_time.append(tree.xpath('//span[@id="system-time"]/text()'))
			wan_status.append(tree.xpath('//span[@id="wan-status"] //font /text()'))
			sdcard_status.append(tree.xpath('//span[@id="sdcard-status"] //font /text()'))	

		except  Exception, e:
			bluetooth_logger.append('---')
			system_time.append('----')
			wan_status.append('----')
			sdcard_status.append('----')

		try:
			s1 = requests.Session()
			r1=s1.get('http://xxxxxxx'+str(iTravel)+'xxxxxxx', auth=HTTPBasicAuth('xxxxxxx', 'xxxxxxx'))	
			tree = r1.text
			m = re.search('READ', tree)
			if m:
				bluetooth_status.append('READ/WRITE OK')
			else:
				bluetooth_status.append('---')
	
		except  Exception, e:
			bluetooth_status.append('---')


	full_list=[]
	for i in range(0, len(iTravel_list)):
		full_list.append([iTravel_list[i],bluetooth_logger[i],bluetooth_status[i],system_time[i],wan_status[i],sdcard_status[i]])

	return full_list
