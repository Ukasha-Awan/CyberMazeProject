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
    path('cloud-recon',views.cloudrecon,name="cloud-recon"),
    path('NS3',views.NS3,name="NS3"),
    path('NS4',views.NS4,name="NS4"),
    path('NS5',views.NS5,name="NS5"),
    path('crypt2',views.crypt2,name="crypt2"),
]
