from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import RegisterUser  # <- Import RegisterUser view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/auth/register/', RegisterUser.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Task endpoints
    path('api/tasks/', include('tasks.urls')),
]
