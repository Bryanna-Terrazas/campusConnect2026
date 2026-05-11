from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('social/', views.social, name='social'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/edit/<int:event_id>/', views.event_edit, name='event_edit'),
    path('events/delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('messages/', views.messages_page, name='messages'),
    path('social/edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('social/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    
]
