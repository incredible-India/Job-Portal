from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from . import forms
from django.db.models import Q
from django.contrib import messages
from .models import UserProfile
from django.utils.decorators import method_decorator
from .middleware  import checkingUserAuthentication
# Create your views here.
class newUser(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth == False:
            form = forms.RegistrationForm()
            return render(request, 'user/newUser.html', {'form': form})
        else:
            return redirect('/')
    def  post(self,request):
        if request.method == 'POST':
            print(request)
            form = forms.RegistrationForm(request.POST, request.FILES)  # Including request.FILES for image upload
            if form.is_valid():
                form.save()  # Save the form data to the database
                request.session['email'] = request.POST["email"] 
                request.session['name'] = request.POST['full_name']
                return redirect('/')
            else:
                return render(request, 'user/newUser.html', {'form': form})



class login(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth == False:
            return render(request,'user/login.html')
        else:
            return redirect('/')
    
    
    def post(self,request):
        email  =  request.POST['email']
        password = request.POST["password"]

        isUser =  UserProfile.objects.filter(Q(email = email) & Q(password = password))
        
        if(len(isUser)==1):
            userinfo = UserProfile.objects.get(Q(email = email))
            request.session['email'] = email 
            request.session['name'] = userinfo.full_name
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/user/login')

        
class logout(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            del request.session['name']
            del request.session['email']
   
        
        return HttpResponseRedirect('/')
        