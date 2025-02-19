from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('detail/', views.detail, name='detail'),
    path('index/', views.index, name='index'),
    path('update/', views.update, name='update'),

]