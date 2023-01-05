from django.urls import path
from user import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
     
    path('signin/', auth_view.LoginView.as_view(template_name = 'user/login.html'), name='signin'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
   
]