"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from firstweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('calpage/',views.CalPage),
    path('cal/',views.Cal),
    path('wordcloud/',views.wordcloud),
    path('gwordcloud/',views.gwordcloud),
    path('sample/',views.sample),
    path('samplecity/',views.samplecity),
    path('citycor/',views.citycor),
    path('citycorrect/',views.citycorrect),
    path('visu/',views.visu),
    path('yancheng/',views.yancheng)
]