from django.views.generic import ListView, DetailView
from .models import *


class FuncLilstView(ListView):
    model = Functionalities
    template_name='func/func_list.html'
    context_object_name='func_list'

class FuncDetailView(DetailView):
    model = Functionalities
    template_name = 'func/func_detailview.html'