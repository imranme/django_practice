from . import views
from django.urls import path

urlpatterns = [
    path('',views.show_item,name ='show_item'),
]


