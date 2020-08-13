from django.shortcuts import render
from django.http import HttpResponse

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"rsk/get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"rsk/post_demo.html")