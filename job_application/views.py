from django.shortcuts import render
from .forms import Application_form
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
        print(first_name)
        print(last_name)
        print(email)
        print(date)
    return render(request,"index.html")