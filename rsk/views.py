from django.shortcuts import render,redirect
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

        return redirect("rsk:home")
        #return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,password,phno,date,month,year,gender))
    return render(request,"registration.html")

def multi(request):
    if request.method=="POST":

        food=request.POST.getlist("food")
        languages=request.POST.getlist("languages")
        
        return HttpResponse("<h1>{}{}</h1>".format(food,languages))
    return render(request,"multiselect.html")

from django.core.files.storage import FileSystemStorage

def img(request):
   
    return render(request,"img_upload.html")


from rsk.utilities import store_image

def img_disp(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image1=request.FILES.get('karthi1')
        image2=request.FILES.get('karthi2')
        file_urls=map(store_image,[image1,image2])

    return render(request,"img_display.html",context={'file_urls':file_urls})

from rsk import forms

def builtinforms(request):
    form=forms.sampleForm(request.POST,request.FILES) 
    if form.is_valid():
        first_name=form.cleaned_data.get('first_name')
        last_name=form.cleaned_data.get('last_name')
        email=form.cleaned_data.get('email')
        phno=form.cleaned_data.get('phno')
        pwd=form.cleaned_data.get('pwd')
        birth_day=form.cleaned_data.get('birth_day')
        birth_month=form.cleaned_data.get('birth_month')
        birth_year=form.cleaned_data.get('birth_year')
        gender=form.cleaned_data.get('gender')
        image=form.cleaned_data.get('image')
        store_image(image)
        data=form.cleaned_data
        return render(request,"display_data.html",context=data)

    form=forms.sampleForm()
    return render(request,'builtin.html',{'form':form})

#forms is a file or a library 
#in forms Form is a class so we inherit from forms.Form