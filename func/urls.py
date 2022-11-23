from django.urls import path
from . import views
urlpatterns = [
    path('',views.FuncLilstView.as_view(), name = 'func_list'),
    path('detail/<int:pk>',views.DetailView.as_view(), name = 'func_detail'),
   
]
