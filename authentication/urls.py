from .views import Register,VerifyEmail,Login,LogoutAPIView
from django.urls import path, include

urlpatterns = [
    path('register/', Register.as_view(),name="register"),
    path('email-verify/',VerifyEmail.as_view(),name="email-verify"),
    path('login/', Login.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout"),

]