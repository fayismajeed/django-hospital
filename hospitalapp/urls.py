from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('booking',views.booking,name='book'),
    path('doctors',views.doctors,name='doct'),
    path('dep',views.department,name='dep'),
    path('contact',views.contact,name='cont'),    
 ]