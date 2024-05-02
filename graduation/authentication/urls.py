from django.urls import path, include
from unicodedata import name
from .views import (
        RegisterUserView, 
        VerifyUserEmail,
        LoginUserView, 
        TestingAuthenticatedReq, 
        PasswordResetConfirm, 
        PasswordResetRequestView,SetNewPasswordView, LogoutApiView)
from rest_framework_simplejwt.views import (TokenRefreshView,)
# from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenRefreshView

# router = DefaultRouter()

urlpatterns = [
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('get-something/', TestingAuthenticatedReq.as_view(), name='just-for-testing'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='reset-password-confirm'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
    path('logout/', LogoutApiView.as_view(), name='logout')
]