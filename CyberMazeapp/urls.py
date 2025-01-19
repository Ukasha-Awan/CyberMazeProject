from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
#from .views import (TeamListView)


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

    path('update-score/', views.update_score, name='update_score'),
    path('get-score/', views.get_score, name='get_score'),

    path('crypt4',views.crypt4,name="crypt4"),
    path('levelList1',views.levelList1,name="levelList1"),
    path('levelList2',views.levelList2,name="levelList2"),
    path('levelList3',views.levelList3,name="levelList3"),
    path('levelList4',views.levelList4,name="levelList4"),

    path('base',views.base,name="base"),
    
    #path("teams/", TeamListView.as_view(), name="team_members"),

]
