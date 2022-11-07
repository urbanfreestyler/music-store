
from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.home, name='home'),

    path('checkout/<int:id>/', views.checkout, name="checkout"),
    path('delivery/<int:id>/', views.delivery, name="delivery"),
    path('send_mail/<int:id>/', views.send_mail, name='send_mail'),

    path('contact/', views.contact_us, name="contact"),

    path('register', views.registration, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name="logout"),

    #REST_FRAMEWORK_URL
    path('apiaccount/register', views.registerPage, name='api_register'),
    path('api/login/', obtain_auth_token, name="api_login"),

    path('beats/', views.beat_list, name='beat-list'),
    path('beats/<int:pk>/', views.beat_detail, name='beat-detail'),
]