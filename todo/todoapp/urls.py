from django.urls import path
from .views import *


urlpatterns=[
    path('delm<int:id>',DelTodo.as_view(),name="delm"),
    path('signup',SignUp.as_view(),name="signup"),
    path('lgout',LgOut.as_view(),name="lgout"),

]