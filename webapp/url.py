from django.urls import path
from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',view.login,name="login"),
]
