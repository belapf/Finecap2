"""
URL configuration for main project.

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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from principal.views import IndexView, ReservaCreateView, ReservaDeleteView, ReservasListView, ReservaUpdateView, StandCreateView, StandDeleteView, StandListView, StandUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('reserva/', ReservaCreateView.as_view(),name='reserva_criar'),
    path('reserva/editar/<int:pk>/', ReservaUpdateView.as_view(), name='reserva_editar'),
    path('reserva/remover/<int:pk>/', ReservaDeleteView.as_view(),name='reserva_remover'),
    path('reserva/listar', ReservasListView.as_view(),name='reserva_listar'),

    path('stand/', StandListView.as_view(), name ='stand_listar'),
    path('stand/criar', StandCreateView.as_view(), name= 'stand_criar' ),
    path('stand/editar/<int:pk>/', StandUpdateView.as_view(), name='stand_editar'),
    path('stand/remover/<int:pk>/', StandDeleteView.as_view(),name='stand_remover'),

    path('accounts/', include('allauth.urls')),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
