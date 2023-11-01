from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aktuality/', views.aktuality, name='aktuality'),
    path('organizaceskoly/', views.organizaceskoly, name='aorganizaceskoly'),
    path('organizaceroku/', views.organizaceroku, name='organizaceroku'),
    path('zapisprvnitrida/', views.zapisprvnitrida, name='zapisprvnitrida'),
    path('poradny/', views.poradny, name='poradny'),
    path('zamestnanci/', views.zamestnanci, name='zamestnanci'),
    path('dokumenty/', views.dokumenty, name='dokumenty'),
    path('historie/', views.historie, name='historie'),
    path('projekty/', views.projekty, name='projekty'),
    path('dokumenty_ms/', views.projekty, name='dokumenty_ms'),
    path('ms/', views.projekty, name='ms'),
    path('projekty_ms/', views.projekty, name='projekty_ms'),
    path('zapis_ms/', views.projekty, name='zapis_ms'),
    path('jidelna/', views.projekty, name='jidelna'),
    path('kontakt/', views.projekty, name='kontakt'),

]