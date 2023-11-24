"""
URL configuration for projecta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from projecta import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/',views.contacts),
    path('',views.home,name="home"),
    path('achievements',views.achievements),
    path('name/<slug:name>',views.name),
    path('location/',views.location),
    path('ourclients/',views.clients),
    path('ourmanagement/',views.management),
    path('vote/<slug:ans>',views.vote),
    path('Resorts',views.Resorts),
    path('gallary',views.gallary),
    path('form',views.userform ),
    path('regi/',include('registration.urls')),
    path('ourservice/',include('ourservice.urls')),
    path('product/',include('Product.urls')),

    # path('review/',include('review.urls')),
    # path('inputreview/',include('review.urls')),
    # path('contacts/'views.about,name='cnt')
    # path('locdemo/',views.locdemo),
    # path('managementdemo/',views.managementdemo),
    # path('Resort/',views.Resort),
    # path('Resort/',views.Resort),
    # path('clientsdemo/',views.clientsdemo),
    
]
