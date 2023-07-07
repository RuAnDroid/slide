from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('projects/<str:pk>/', views.projects, name="projects"),
    path('single-card/<str:pk>', views.single_card, name="single-card"),
    path('create-project/', views.create_project, name="create-project"),
    path('update-project/<str:pk>/', views.update_project, name="update-project"),
    path('delete-project/<str:pk>/', views.delete_project, name="delete-project"),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]


