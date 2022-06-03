"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    
    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    # Because URL paths are loaded top-to-bottom placing the auth path above the accounts path ensures that auth paths will be loaded first.
    # And when the auth path can't resolve my login url, it'll search for it in the accounts url (where the custom login view resides)
    path('accounts/', include('accounts.urls')),
]
