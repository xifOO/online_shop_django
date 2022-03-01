"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from accounts.views import Register
from boots.views import order_app, project_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('boots/', include(('boots.urls', 'boots'), namespace='boots')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('mailings/', include(('mailings.urls', 'mailings'), namespace='mailings')),
    path('search', include(('search.urls', 'search'), namespace='search')),
    path('', order_app, name='home'),
    path('project_info', project_info, name='project_info'),

]


handler404 = 'boots.views.page_not_found_view'