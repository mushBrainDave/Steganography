from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:message_id>/', views.message, name='message'),
    path('name/', views.get_name, name='name')
]
