from django.contrib import admin
from django.urls import path, include
from home import views


admin.site.site_header = "AJ Bike Modification Admin"
admin.site.site_title = "AJ Bike Modification Admin Portal"
admin.site.index_title = "Welcome to AJ Bike Modification Portal"


urlpatterns = [
    path("", views.index, name= 'home'),
    path("about", views.about, name= 'about'),
    path("gallery", views.gallery, name= 'gallery'),
    path("services", views.services, name= 'services'),
    path("contact", views.contact, name= 'contact'),
]
