from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json

# Create your views here.
def index(request):
	test = 'test'
	context = {
		'test': json.dumps(test)
	}
	return render(request, 'headbone/index.html', context)