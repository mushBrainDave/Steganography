from django.urls import path
from . import views


app_name = 'client'
urlpatterns = [
    path('thanks', views.success, name='success'),
    path('image_upload', views.image_view, name='image_form'),
]
