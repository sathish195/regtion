from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegForm,LoginForm
from .models import Reg
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        r_f=RegForm
        return render(request,'reginput.html',{'reg_form':r_f})
class RegInsert(View):
    def post(self,request):
        r_f=RegForm(request.POST)
        if r_f.is_valid():
            r_f.save()
        return HttpResponse('registion success')
class LoginInput(View):
    def get(self,request):
        l_f=LoginForm
        return render(request,'logininput.html',{'login_form':l_f})
class LoginInserf(View):
    def post(self,request):
        MyLoginForm=LoginForm(request.POST)
        if MyLoginForm.is_valid():
            user=MyLoginForm.cleaned_data['username']
            passw=MyLoginForm.cleaned_data['password']
            dbuser=Reg.objects.filter(username=user,password=passw)
            if not dbuser:
                return HttpResponse('<html><body bgcolor=red><h1>login faild</h1></body></html>')
            else:
                return HttpResponse('<html><body bgcolor=green><h1>login sucess</h1></body></html>')