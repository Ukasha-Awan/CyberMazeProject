from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
from .views import update_score

urlpatterns = [
    path('',views.index,name="index"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="blog"),
    path('domains/',views.domains,name="domains"),
    path('level1/',views.level1,name="level1"),
    path('crypt1/',views.crypt1,name="crypt1"),
   
    path('NS2',views.NS2,name="NS2"),
    path('cloud-recon',views.cloudrecon,name="cloud-recon"),
    path('trailoftroubles',views.trailoftroubles,name="trailoftroubles"),
    path('NS3',views.NS3,name="NS3"),
    path('NS4',views.NS4,name="NS4"),
    path('NS5',views.NS5,name="NS5"),
    path('NS6',views.NS6,name="NS6"),
    path('crypt2',views.crypt2,name="crypt2"),
    path('crypt3',views.crypt3,name="crypt3"),

    path('update-score/', update_score, name='update_score'),
]
