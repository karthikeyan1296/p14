from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail



def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"rsk/home.html")

def profile(request):
    name="karthi"
    return render(request,"rsk/profile.html",{'name':name})


def get_demo(request):
    name=request.GET.get('name')
    return render(request,"rsk/get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"rsk/post_demo.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")

        send_mail("thanks for registration","hello Mr./Ms{} {}\n Thanks for Registering".format(first_name,last_name),
        "karthikeyanrs1260@gmail.com",[email,],fail_silently=False)

        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,password,phno,date,month,year,gender))
    return render(request,"registration.html")

def multi(request):
    if request.method=="POST":

        food=request.POST.getlist("food")
        languages=request.POST.getlist("languages")
        
        return HttpResponse("<h1>{}{}</h1>".format(food,languages))
    return render(request,"multiselect.html")

from django.core.files.storage import FileSystemStorage

def img(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['karthi']
        print(image)
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)

    return render(request,"img_upload.html",context={'file_url':file_url})