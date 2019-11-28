from django.urls import path

from . import views
from .views import SimpleCandlestickWithPandas

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', SimpleCandlestickWithPandas.as_view(),name='simple-candlestick'),
]