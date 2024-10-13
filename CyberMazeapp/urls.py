from django.urls import path
from CyberMazeapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('domains',views.domains,name="domains"),
    path('level1',views.level1,name="level1"),
    path('crypt1',views.crypt1,name="crypt1"),
    path('login',views.login,name="login"),
    path('NS2',views.NS2,name="NS2"),
]
