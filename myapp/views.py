from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def counter(request):
    text=request.POST['text']
    total = len(text.split())
    return render(request,"counter.html",{ 'total':total } )

