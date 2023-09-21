from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('code-generation/', views.code_generation_view, name='code_generation_view'),
]
