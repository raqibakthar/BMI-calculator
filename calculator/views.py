from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def calculator(request):
    context=None
    try:
        if request.method == 'POST':
            height=int(request.POST.get('height'))
            weight=int(request.POST.get('weight'))
            result=weight/(height/100)**2
            bmi=round(result,3)
            context={
                'bmi':bmi,
            }
    except ValueError:
        messages.error(request, 'Type the fields before calculate')
    return render(request,'calculator.html',context)

