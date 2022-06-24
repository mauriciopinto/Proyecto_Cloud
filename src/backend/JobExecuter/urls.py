from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'run_jobs', views.ExecutedJobViewSet)
router.register(r'status', views.StatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('execute/', views.run_job),
    path('output/', views.get_output_file)
]