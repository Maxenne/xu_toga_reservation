from django.urls import path
from . import views

urlpatterns = [
    path('api/reserve/', views.reserve_toga, name='reserve_toga'),
]