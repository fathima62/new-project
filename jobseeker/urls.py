from django.urls import path

from . import views
app_name='jbskr'
urlpatterns=[
    path('',views.login,name='login'),
    path('srch',views.search,name='search'),
    path('detls',views.details,name='details'),

]