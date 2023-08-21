from django.urls import path
from .views import *

urlpatterns = [
    path('nothing/<int:user_id>/', what)
]