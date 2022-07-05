from django.urls import path

from . import views

app_name='emplyer'

urlpatterns=[
    path('emplyrlogin',views.login,name="emplylogin"),
    path('emplyrhome',views.home,name="emplyhome")
]