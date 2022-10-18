from django.shortcuts import render,HttpResponse,redirect
from .models import Messagebox,getintouch
from app.forms import Form1,Form2
import requests

# Create your views here.

def home(request):
    if request.method == 'POST':
        c_name = request.POST['c_name']
        c_phone = request.POST['c_phone']
        c_email = request.POST['c_email']
        text = request.POST['text']
        newdata = getintouch(c_name=c_name,c_phone=c_phone,c_email=c_email,text=text)
        newdata.save()

        task = getintouch.objects.get(pk=newdata.pk)

        Client_Name = task.c_name
        Client_Mail = task.text

        http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client_Name + " for " + Client_Mail + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
        requests.get(http_req)

        #return render(request,'thankyou.html')
        return redirect('/')
        #return HttpResponse("Sent Message!!!")
    return render(request,'home.html')

