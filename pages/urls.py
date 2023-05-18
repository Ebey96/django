from django.urls import path
from . import views

urlpatterns = [
    path('',views.h1,name='h1'),
    path('h2',views.h2, name="h2"),
    path('h3',views.h3, name="h3"),
    path('Scénario',views.Scénario, name="Scénario"),
    path('s1',views.s1, name="s1")
    
]