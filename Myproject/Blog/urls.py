from django.urls import path
from . import views
app_name='Blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.details, name='details')
]