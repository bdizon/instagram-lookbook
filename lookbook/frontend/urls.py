from django.urls import path
from .views import index

urlpatterns = [
    path('', index)     # renders index.html template
]