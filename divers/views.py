from django.shortcuts import render
from .functions import multiplicate_by_5



weekdays=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimenche']
# Create your views here.
def home_view(request):
    weekdays=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimenche']
    context={
        'test':'Ceci est un test',
        'multi8': multiplicate_by_5(8),
        'weekdays':weekdays
    }
    # import pudb;pu.db()
    return render(request,'divers/home_page.html',context=context)

def about_view(request):
    return render(request,'divers/about_page.html')

def us(request):
    return render(request,'divers/about_us.html')