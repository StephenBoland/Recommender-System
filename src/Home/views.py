from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from src.Home.forms import RegistrationForm
from tablib import Dataset

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})
def AccountSettings_view(request, *args, **kwargs):
    return render(request, "AccountSettings.html", {})
def Import_view(request, *args, **kwargs):
    return render(request, "Import.html", {})
def Import_Breweryview(request, *args, **kwargs):
    return render(request, "ImportBrewery.html", {})
def base_view(request, *args, **kwargs):
    return render(request,"base.html", {})
def logged_in_view(request, *args, **kwargs):
    return render(request, "logged_in.html",{})

#login and registration forms
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid(): #is the form valid? filled out properly
            user = form.save() #save the users detail
            login(request, user)
            return redirect("/home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            
    
    form = RegistrationForm()
    return render(request,
                  "register.html",
                  context={"form":form})




#uploading csv file for beer database
def simple_upload(request):
    if request.method == 'POST':
        file_format = request.POST['file_format']
        beer_resource = BeerInformation()
        dataset = Dataset()
        new_beer = request.FILES['importData']
        
        
        if file_format == 'CSV':
            imported_data = dataset.load(new_beers.read().decode('utf-8'),format='csv')
            result = beer_resource.import_data(dataset, dry_run=True)
        elif file_format =='JSON':
            imported_data = dataset.load(new_beers.read().decode('utf-8'),format='json')
            result = beer_resource.import_data(dataset, dry_run=True)
            
        if not result.has_errors():
            beer_resource.import_data(dataset, dry_run=False) 
        
    return render(request, 'Import.html')
#uploading csv file for brewery database
def simple_uploadbrewery(request):
    if request.method == 'POST':
        file_format = request.POST['file_format']
        brewery_resource = BreweryInformation()
        dataset = Dataset()
        new_brewery = request.FILES['importData']
        
        
        if file_format == 'CSV':
            imported_data = dataset.load(new_brewery.read().decode('utf-8'),format='csv')
            result = brewery_resource.import_data(dataset, dry_run=True)
        elif file_format =='JSON':
            imported_data = dataset.load(new_brewery.read().decode('utf-8'),format='json')
            result = brewery_resource.import_data(dataset, dry_run=True)
            
        if not result.has_errors():
            brewery_resource.import_data(dataset, dry_run=False) 
        
    return render(request, 'Importbrewery.html')