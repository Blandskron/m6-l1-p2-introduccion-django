from django.urls import path
from . import views

app_name = 'leccion1'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('python-vs-django/', views.python_vs_django, name='python_vs_django'),
    path('entornos-virtuales/', views.virtual_envs, name='virtual_envs'),
    path('mvc-dry-templates/', views.mvc_dry, name='mvc_dry'),
    path('router-database/', views.router_db, name='router_db'),
    path('dev-vs-prod/', views.dev_vs_prod, name='dev_vs_prod'),
]
