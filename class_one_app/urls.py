from django.urls import path
from .import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', views.home_page),
    path('about/', views.about_page),
    path('contact/', views.contact_page),
    path('all_orders/', views.order_page),
    path('experiment/', views.experiment_page),
    path('experiment/<person>', views.experiment_page),
    
]