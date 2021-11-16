from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from account.models import Services

def create_profile(request, service_id):
    service = get_object_or_404(Services, pk=service_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(
                full_name=form.cleaned_data['full_name'],
                country=form.cleaned_data['country'],
                company=form.cleaned_data['company'],
                phone_no=form.cleaned_data['phone_no'],
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],        
            )
            profile.save()
            service.profile.add(profile)#Add the newly created profile to the service request
            return redirect('account:services')#Redirect to the Service page
    else:
        form = ProfileForm() 
    context = {
        'form': form,
        'service': service,
        #'profile': profile,#You may not want to display a contact message/returns the newly created profile object
    }           
    return render(request, 'company_profile/request-service.html', context)


