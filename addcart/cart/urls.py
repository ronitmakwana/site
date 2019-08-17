from django.urls import path
from .views import pro,proview


urlpatterns = [
    path('',pro),
    path('proview/',proview),
    
]
