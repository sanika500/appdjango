from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name="index"),
    path('delete/<int:pk>/',views.delete_g,name='delete_g'),
]