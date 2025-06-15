from django.contrib import admin
from django.urls import path, include
from tracker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>/edit/', views.edit_file, name='edit_file'),
    path('files/<int:file_id>/history/', views.file_history, name='file_history'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

