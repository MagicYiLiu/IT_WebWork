from django.urls import path, include
from .import views

app_name = "myApp"
urlpatterns = [

    # Paths for the homepage and base page
    path('', views.home, name='Homepage'),
    path('about/', views.about, name='About'),
    path('edit/<forloop_counter>', views.edit, name='Edit'),
    path('del/<forloop_counter>', views.delete, name='Delete'),
    path('cross/<forloop_counter>', views.cross, name='Done'),

    # Paths for the 'Sign in' 'Register' and 'tips'.
    path('graphic/', views.graphic,name= "Graphic"),
    path('video/', views.video,name= "Video"),
    path('signIn/', views.signIn,name= "SignIn"),
    path('signOut/', views.signOut,name= "SignOut"),
    path('register/', views.gotoRegister,name= "Register"),

    # Paths for the graphic tips
    path('graphic/graphic_31days/', views.graphic_31days,name= "graphic_31days"),
    path('graphic/graphic_Abs', views.graphic_Abs, name= "graphic_Abs"),
    path('graphic/graphic_Arms', views.graphic_Arms, name= "graphic_Arms"),

]
