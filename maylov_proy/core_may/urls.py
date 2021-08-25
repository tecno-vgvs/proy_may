from django.urls import path
from core_may.views import home, inicio, presente, futuro
urlpatterns = [
    path('', home, name="home"),
    path('inicio',inicio, name="inicio"),
    path('presente', presente, name="presente"),
    path('futuro', futuro, name="futuro")
]