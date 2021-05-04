from django.shortcuts import render
from myapp.forms import *
from myapp.models import *
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        form = MedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Image is saved")
    else:
        form = MedForm()
    context={'form':form}
    return render(request, 'home.html', context)