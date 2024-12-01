
from django.urls import path 
from . import views 


urlpatterns = [

    path('new-user/',views.newUser.as_view()),
        path('login/',views.login.as_view()),
        path('logout/',views.logout.as_view())

]
