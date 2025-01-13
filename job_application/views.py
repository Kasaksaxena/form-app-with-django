from django.shortcuts import render
from .forms import Application_form
from .models import Form
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=="POST":
      form=Application_form(request.POST)
      if form.is_valid():  
#in cleaned-data values are already cleaned and type-cast(like strings for textfield and integers for no.fields)           
        first_name=form.cleaned_data["fname"]
        last_name=form.cleaned_data["lname"]
        email=form.cleaned_data["email"]
        date=form.cleaned_data["date"]
        occupation=form.cleaned_data["occupation"]
        
        Form.objects.create(first_name=first_name,last_name=last_name,email=email,
                            date=date,occupation=occupation)
        
        messages.success(request,"Form submitteed successfully")
    return render(request,"index.html")