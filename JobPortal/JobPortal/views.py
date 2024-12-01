from django.shortcuts import render
from user.middleware import checkingUserAuthentication
from django.utils.decorators import method_decorator
from django.views import View


class index(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            return render(request,"homepage.html")
        else:
            return render(request,"index.html")

    