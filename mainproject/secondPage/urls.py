from django.urls import path

from secondPage import views

urlpatterns = [

       path('second/', views.second),
       path('addStudents/', views.add_student),
       path('getStudents/', views.get_student),
]