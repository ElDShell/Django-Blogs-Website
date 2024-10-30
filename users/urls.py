from django.urls import path
from .views import * 
urlpatterns = [
    # Users 
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    
    # Users Password
    path('change_password/<int:pk>/',ChagePasswrod.as_view(),name='change_password'),
    path('password/reset/',ResetPasswordView.as_view(),name='password_reset'),
    path('password/reset/done/',ResetPasswordDoneView.as_view(),name='password_reset_done'),
    # path('password/reset/confirm/<uidb64>/<token>-<timestamp>/',ResetPasswordConfirmView.as_view(),name='password_reset_confirm'),
    path('password/reset/confirm/<uidb64>/<token>/',ResetPasswordConfirmView.as_view(),name='password_reset_confirm'),
    
    # User Profile
    path('profile/<int:pk>/content/',ProfileDetial.as_view(),name='profile_content'),
    path('profile/<int:pk>/update/',ProfileUpdate.as_view(),name='profile_update'),
    path('profile/img/<int:pk>/update/',ProfileImageUpdateView.as_view(),name='profile_image_update'),
    path('profile/img/<int:pk>/delete/',ProfileImageDeleteView.as_view(),name='profile_image_delete'),
]

