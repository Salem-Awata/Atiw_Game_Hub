from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('<slug:slug>/', views.play_game, name='play_game'),
    path('<slug:slug>/submit_score/', views.submit_score, name='submit_score'),
]
