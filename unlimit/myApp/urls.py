from django.urls import path, include
from .import views

app_name = "myApp"
urlpatterns = [
    path('', views.home, name='Homepage'),
    path('about/', views.about, name='About'),
    path('edit/<forloop_counter>', views.edit, name='Edit'),
    path('del/<forloop_counter>', views.delete, name='Delete'),
    path('cross/<forloop_counter>', views.cross, name='Done'),

    path('graphic/', views.graphic,name= "Graphic"),
    path('video/', views.video,name= "Video"),
    path('signIn/', views.signIn,name= "SignIn"),
    path('signOut/', views.signOut,name= "SignOut"),
    path('register/', views.gotoRegister,name= "Register"),


]