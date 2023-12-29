from django.conf.urls.static import static, settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('collection/', views.collection, name='collection'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
