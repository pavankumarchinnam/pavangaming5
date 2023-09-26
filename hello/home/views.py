from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        "variable":"I am ironman"
    }
    return render(request,'index.html',context)
    # return HttpResponse("avengers assemble")
def about(request):
    return render(request,'about.html')
   # return HttpResponse("this is about")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phno=phno,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse("contact mr.pavan 9757382763782")
def games(request):
     return render(request,'games.html')
   # return HttpResponse("which game do you want god or gta5")