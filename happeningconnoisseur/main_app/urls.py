from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_index, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='index'),
    path('events/<int:event_id>/', views.events_detail, name='detail'),
    path('events/add/', views.events_add, name='add'),
    path('vendors/', views.vendors_index, name='vendors_index'),
    path('events/<int:event_id>/assoc_vendor/<int:vendor_id>/', views.assoc_vendor, name='assoc_vendor'),
]
