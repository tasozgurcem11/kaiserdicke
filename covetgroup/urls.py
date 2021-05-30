from django.urls import path
from covetgroup import views

urlpatterns = [
    path('', views.index),
    path('impressum/', views.impressum),
    path('datenschutz/', views.datenschutz),
    # path('download_pdf/', views.download_pdf, name="download_pdf")
]
