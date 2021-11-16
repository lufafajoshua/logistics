from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Location, Services, Contact
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactForm
from company_profile.models import Profile


def index(request):#This is the home page sample
    return render(request, 'account/index.html')

def account(request):#Display the account based on its Id
    company_account = Account.objects.all()#Get all account objects since its only one
    services = Services.objects.all()#Get all the services objects for display in the home page
    contacts = Contact.objects.all()#Might consider not showing this in the user page
    location = Location.objects.all()#All the location objects for display in the home page
    context = {
        'accounts': company_account,
        'services': services,
        'contacts': contacts,
        'location': location,
    }
    return render(request, 'logistics1/index.html', context)#display this on the homepage 

def view_account(request, account_id):#Display the account based on its Id
    company_account = get_object_or_404(Account, pk=account_id)#Get all account objects since its only one
    context = {
        'account': company_account,
    }
    return render(request, 'account/home.html', context)#display this on the homepage 

def services(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'logistics1/service.html', context)

def service(request, service_id):#View a specific service along with its description
    service = get_object_or_404(Services, pk=service_id)
    context = {
        'service': service,
    } 
    return render(request, 'logistics1/single-service.html', context)
#First set out the examples in the frontend before making changes to the real site
def air_freight(request, service_id):#This will get the specified service with the id and then pass it to its own special page instead of sending to one service page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/air-freight.html', context)

#Create other services pages and redirect them to their respective pages
def transportation(request, service_id):
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/transportation.html', context)

def consultancy(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/consultancy.html', context)

def seafreight(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/sea-freight.html', context)

def airfreight(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/airfreight.html', context)


def clearance(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/customs.html', context)


def parking(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/parking.html', context)


def roadfreight(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/road-freight.html', context)

def railfreight(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/railway-freight.html', context)

def warehouse(request, service_id):#This will display the tax consultancy page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/warehouse.html', context)


def cargo(request, service_id):#Cargo handling
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/cargo.html', context)

def supplies(request, service_id):#General supplies
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/supplies.html', context)

def storage(request, service_id):#cargo-storage
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/storage.html', context)

def logistics(request, service_id):#This will display the logistics page
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/logistics.html', context)

def transfer(request, service_id):#Money Transfer page detail
    service = get_object_or_404(Services, pk=service_id)
    services = Services.objects.all()
    context = {
        'service': service,
        'services': services,
    } 
    return render(request, 'logistics1/services/transfer.html', context)

def create_contact(request):#Create the contact form and submit the data to the backend for processing
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact.save()
            return redirect('account:index')
    else:
        form = ContactForm() 
    context = {
        'form': form,
        #'contact': contact,#You may not want to display a contact message
    }           
    return render(request, 'logistics1/contact.html', context)

def blog(request):
    return render(request, 'logistics1/blog.html')

def airblog(request):#This poits to the blog app and not the service 
    return render(request, 'logistics1/blog/air-freight.html')

def cargoblog(request):#This points to the blog about the ocean freight
    return render(request, 'logistics1/blog/cargo.html')

def consultancyblog(request):
    return render(request, 'logistics1/blog/consultancy.html')

def logisticsblog(request):#This points to the blog about the ocean freight
    return render(request, 'logistics1/blog/logistics.html')

def storageblog(request):#This points to the blog about the ocean freight
    return render(request, 'logistics1/blog/storage.html')

def suppliesblog(request):#This points to the blog about the ocean freight
    return render(request, 'logistics1/blog/supplies.html')

def transferblog(request):#This points to the blog about the ocean freight
    return render(request, 'logistics1/blog/transfer.html')

def transportationblog(request):#This points to the blog about the ocean freight
    return render(request, 'logistics1/blog/transportation.html')

def about(request):
    return render(request, 'logistics1/about.html')    

def about_team(request):
    return render(request, 'logistics1/about-team.html')

def about_support(request):
    return render(request, 'logistics1/about-support.html')

def about_profile(request):
    return render(request, 'logistics1/about-company-profile.html') 

def about_history(request):
    return render(request, 'logistics1/about-company-history.html')           

def location(request):
    return render(request, 'logistics1/location.html')