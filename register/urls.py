from register import views
from django.urls import path

urlpatterns = [
    path('form/', views.register)
]
