from django.shortcuts import render
from myapp1.models import Gallery


def home(request):
    gallerys = Gallery.objects   # 把Gallery的所有对象都取过来
    return render(request,'home.html',{"gallerys": gallerys})