from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)
from accounts.views import (
    registration_view,
    ChangePasswordView,
    AccountRetrieveUpdateDestroy
)

urlpatterns = [
    # path('auth', include('rest_auth.urls')),
    path('auth/sign_up', registration_view),
    path('auth/login', obtain_jwt_token),
    path('auth/refresh-token', refresh_jwt_token),
    path('auth/verify-token', verify_jwt_token),
    path('auth/change_password/<int:pk>', ChangePasswordView.as_view()),
    path('auth/update_profile/<int:account_id>',
         AccountRetrieveUpdateDestroy.as_view())
]
