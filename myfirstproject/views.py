from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET ['fulltextarea']
    datas=data.split()
    a=len(datas)
    return render(request,'count.html',{'fulltext':data,'word':a})

def aboutus(request):
    return render(request,'aboutus.html')