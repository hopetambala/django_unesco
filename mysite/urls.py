"""mysite URL Configuration

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
'''
Old
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('heritagesites/')),
    path('admin/', admin.site.urls),
    path('heritagesites/', include('heritagesites.urls')),
]
'''
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import path, include

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('heritagesites/')),
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
         name='logout'),
    path('heritagesites/api/rest-auth/', include('rest_auth.urls')),
    path('heritagesites/api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('heritagesites/', include('heritagesites.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('heritagesites/api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# the api-auth route adds log in/log out functionality to the browsable API.