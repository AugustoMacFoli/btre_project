from django.shortcuts import render

def index(request):
    return render(request, 'realtors/realtors.html')

def listing(request):
    return render(request, 'realtors/realtor.html')