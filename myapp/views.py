# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
import os,sys

@csrf_exempt
def test_api(requests):
	print ("test_api page hitted : ", requests)
	if requests.method == 'POST':
		try:
			data = json.loads(requests.body.decode('utf-8'))
			email = str(data['email'])

			response = {'status': 200, 'type': "Hey "+email}
			return JsonResponse(response)
		
		except Exception as e:
			response = {'status': 400, 'error': 'Bad requests!'}
			return JsonResponse(response)