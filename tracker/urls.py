from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('edit/<int:file_id>/', views.edit_file, name='edit_file'),
    path('history/<int:file_id>/', views.file_history, name='file_history'),
]

