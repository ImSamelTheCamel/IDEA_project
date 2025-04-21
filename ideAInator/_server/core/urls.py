from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path('home/', views.home, name="home"),
    path('chat/', views.chat, name="chat"),
    path('profile/', views.profile_view, name='profile'),
    path('save_conversation/', views.save_conversation, name='save_conversation'),
    path('upload/', views.upload_file, name='upload_file'),
    path('transcript/<id>/', views.transcript_view, name='transcript'),
]