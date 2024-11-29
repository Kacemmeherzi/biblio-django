from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.liste_livres, name='liste_livres'),
    path('create/', views.create_livre, name='create'),
    path('livre/delete/<int:pk>/', views.delete_livre, name='delete_livre'),
    path('livre/update/<int:pk>/', views.update_livre, name='update_livre'),


]