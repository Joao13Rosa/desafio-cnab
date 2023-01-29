from django.urls import path
from cnab import views

urlpatterns = [
    path("cnab/", views.upload_file),
    path("cnab/lista/", views.list_operations),
]