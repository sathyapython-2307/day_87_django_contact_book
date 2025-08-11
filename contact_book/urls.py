from django.contrib import admin
from django.urls import path, include
from contacts import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_views.contact_list, name='contact_list'),
    path('add/', contact_views.add_contact, name='add_contact'),
    path('feedback/', contact_views.feedback, name='feedback'),
]
