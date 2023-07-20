from django.urls import path

from . import views

urlpatterns = [


    path('', views.field,name='index1'),
    path('submit/', views.my_form,name='submit'),
    path('view/', views.view_form,name='view'),
    path('delete<int:id>', views.del_form,name='del'),
    path('<int:id>', views.update_form,name='update'),
      

]