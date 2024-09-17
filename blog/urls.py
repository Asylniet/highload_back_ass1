from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post_view, name='create_blog_post'),
    path('post/<int:pk>/edit', views.edit_post_view, name='edit_blog_post'),
    path('post/<int:pk>/delete', views.delete_post_view, name='delete_blog_post'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html', next_page='post_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]