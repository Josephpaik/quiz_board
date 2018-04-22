"""quiz_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from boards import views
from accounts import views as accounts_views

urlpatterns = [
    # index page
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),

    # boards
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),

    # accounts
    path('signup/', accounts_views.signup, name='signup'),

    # authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password Reset
    path('reset/',
         auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64:[0-9A-Za-z_\-]+>/<token:[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]