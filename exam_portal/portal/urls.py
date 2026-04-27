from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),   # ✅ ADD THIS
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('form/', views.exam_form, name='exam_form'),
    path('view/', views.view_forms, name='view_forms'),
]