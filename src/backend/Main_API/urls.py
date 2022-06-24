from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'arguments', views.ArgumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.user_login),
    path('session/', views.get_session_user),
    path('logout/', views.close_session)
]