from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.user_post, name='user_post'),
    path('register/', views.register, name='register'),
    path('register-complete/', views.register_compelete, name='register_complete'),
    path('login/', views.user_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='password_change_form.html'),name='password_change'),

    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('edit-profile/', views.edit_user_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),

]