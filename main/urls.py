from django.urls import path
from main import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("upload/", views.upload_csv, name="upload")
]