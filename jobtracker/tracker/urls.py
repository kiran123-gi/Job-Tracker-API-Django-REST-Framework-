from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),
    path('update/<int:id>/', views.update_job, name='update_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
    path('api/', include(router.urls)),
]