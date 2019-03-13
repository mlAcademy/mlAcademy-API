"""mlacademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.http import HttpResponse
from django.template import Context, loader
#from views import HomePageView
from django.shortcuts import render_to_response


def welcome_page(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


urlpatterns = [
    path('api/', include('api.urls')),
    path('query/', include('lessons.urls')),
    path('admin/', admin.site.urls),
    path('', welcome_page)
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)
