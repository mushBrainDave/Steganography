from django.urls import path
from . import views
#from .views import hotel_image_view

app_name = 'client'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:message_id>/', views.message, name='message'),
    path('image_upload', views.hotel_image_view, name='image_form'),

]
