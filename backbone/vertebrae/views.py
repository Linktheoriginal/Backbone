from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
import random

# Create your views here.
def index(request):
	context = {
		'musicurl': random.choice(["https://www.youtube.com/watch?v=XeONF-4mr9M, https://www.youtube.com/watch?v=81i78S1eBFs", "https://www.youtube.com/watch?v=pKv3xfen2BQ", "https://www.youtube.com/watch?v=CAkFSzEy87s", "https://www.youtube.com/watch?v=yk7OXfsiXsc", "https://www.youtube.com/watch?v=XoVCJnyBO0w", "https://www.youtube.com/watch?v=gQSrXNlnu8M", "https://www.youtube.com/watch?v=B8oywk8elfs", "https://www.youtube.com/watch?v=r71iSRA3zYg", "https://www.youtube.com/watch?v=KH9lMBFLu28", "https://www.youtube.com/watch?v=WEdIg_dOVOY"])
	}
	return render(request, 'vertebrae/index/index.html', context)

def c1(request):
	return render(request, 'vertebrae/c1/index.html')

def c2(request):
	return render(request, 'vertebrae/c2/index.html')

def c3(request):
	return render(request, 'vertebrae/c3/index.html')

def c4(request):
	return render(request, 'vertebrae/c4/index.html')

def c5(request):
	return render(request, 'vertebrae/c5/index.html')

def c6(request):
	return render(request, 'vertebrae/c6/index.html')

def c7(request):
	return render(request, 'vertebrae/c7/index.html')

def c8(request):
	return render(request, 'vertebrae/c8/index.html')