from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('createStudent/', views.createStudent, name='createStudent'),
    path('editStudent/<str:stdId>', views.updateStudent, name='editStudent'),
    path('deleteStudent/<str:stdId>', views.deleteStudent, name='deleteStudent')
]