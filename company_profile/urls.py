from django.urls import path, include
from . import views

app_name = 'company_profile'
urlpatterns = [
    path('create_profile/<int:service_id>', views.create_profile, name='create_profile'),
]