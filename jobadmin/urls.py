from django.urls import path

from . import views

app_name='jobadmin'

urlpatterns=[
    
    path('admin_login',views.admin_login,name="admnlogin" ),
    path('signup',views.admin_signup,name="admin_signup"),
    path('emplyers_list',views.emplyers_lst,name="emp_list"),
]