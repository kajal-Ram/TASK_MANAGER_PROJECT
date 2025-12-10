from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterUser

router = DefaultRouter()
router.register('', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('', RegisterUser.as_view(), name='register'),  # /api/auth/register/
]
