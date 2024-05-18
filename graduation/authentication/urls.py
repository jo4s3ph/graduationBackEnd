from django.urls import path, include
from unicodedata import name
from .views import (
    RegisterUserView, 
    VerifyUserEmail,
    LoginUserView,
    LogoutApiView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),  # Register user
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),  # Verify email with OTP
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT tokens
    path('login/', LoginUserView.as_view(), name='login-user'),  # User login
    path('logout/', LogoutApiView.as_view(), name='logout')  # User logout
]
