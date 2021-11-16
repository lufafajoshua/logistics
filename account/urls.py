from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
   #path('', views.index, name='index'),#Make this point to the account view in order to display the home page
   path('', views.account, name='index'),
   path('account/<int:account_id>', views.view_account, name='view_account'),
   path('services', views.services, name='services'),#Dsiplay all the available services
   path('service/<int:service_id>', views.service, name='service'),#View a specific service
   path('create_contact', views.create_contact, name='create_contact'),
   path('blog', views.blog, name='blog'),
   path('cargo-blog', views.cargoblog, name='cargoblog'),
   path('freight-blog', views.airblog, name='airblog'),#Points to the page for the freigh forwarding blog
   path('consultancy-blog', views.consultancyblog, name='consultancyblog'),#Blog for air freight
   path('logistics-blog', views.logisticsblog, name='logisticsblog'),
   path('storage-blog', views.storageblog, name='storageblog'),
   path('supplies-blog', views.suppliesblog, name='suppliesblog'),
   path('transfer-blog', views.transferblog, name='transferblog'),
   path('transportation-blog', views.transportationblog, name='transportationblog'),
   path('freight assistance/<int:service_id>', views.air_freight, name='air_freight'),
   path('transportation/<int:service_id>', views.transportation, name='transportation'),
   path('tax_consultancy/<int:service_id>', views.consultancy, name='consultancy'),
   path('cargo-handling/<int:service_id>', views.cargo, name='cargo'),
   path('general_supplies/<int:service_id>', views.supplies, name='supplies'),
   path('cargo_storage/<int:service_id>', views.storage, name='storage'),
   path('logistics/<int:service_id>', views.logistics, name='logistics'),
   path('money_transfer/<int:service_id>', views.transfer, name='transfer'),
   path('money_transfer/<int:service_id>', views.transfer, name='transfer'),
   path('sea_freight/<int:service_id>', views.seafreight, name='seafreight'),
   path('air_freight/<int:service_id>', views.airfreight, name='airfreight'),
   path('rail_freight/<int:service_id>', views.railfreight, name='railfreight'),
   path('road_transfer/<int:service_id>', views.roadfreight, name='roadfreight'),
   path('warehouse/<int:service_id>', views.warehouse, name='warehouse'),
   path('clearance/<int:service_id>', views.clearance, name='clearance'),
   path('parking/<int:service_id>', views.parking, name='parking'),
   path('about', views.about, name='about'),
   path('about-team', views.about_team, name='about_team'),
   path('about-support', views.about_support, name='about_support'),
   path('about-profile', views.about_profile, name='about_profile'),
   path('about-history', views.about_history, name='about_history'),
   path('location', views.location, name='location'),
]