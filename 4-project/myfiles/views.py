from django.shortcuts import render

# Create your views here.
def home(malumot):
    return render(malumot,'index.html')