"""keysdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views as accounts_views
from boards import views as boards_views
from core import views as core_views

urlpatterns = [
    # Home
    path('', core_views.home, name='home'),
    
    # Account creation/login/logout
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Account password reset
    path('reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    # Account settings - change password
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),
    path('settings/account/done/', accounts_views.my_account_done, name='my_account_done'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    # Boards
    path('boards/', boards_views.BoardListView.as_view(), name='boards'),
    path('boards/<pk>/', boards_views.TopicListView.as_view(), name='board_topics'),
    path('boards/<pk>/new', boards_views.new_topic, name='new_topic'),
    path('boards/<pk>/topics/<topic_pk>/', boards_views.PostListView.as_view(), name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', boards_views.reply_topic, name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit/',
        boards_views.PostUpdateView.as_view(), name='edit_post'),
    
    # Admin
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
]
