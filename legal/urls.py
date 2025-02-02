from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'legal'


urlpatterns = [
    # This is the home page
    path('',views.index,name='index'),
    # This page shows all the case details
    path('cases/',views.cases,name='cases'),
    # Detail page for each case
    path('cases/<int:case_id>/',views.case,name='case'),
    path('new_case/',views.new_case,name='new_case'),
    path('delete_case/<int:case_id>/',views.delete_case,name='delete_case'),
]