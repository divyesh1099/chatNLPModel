from django.urls import path
from . import views
app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('chat-history/', views.chat_history_view, name='chat_history'),
    path('chat/<int:chat_id>/', views.chat_detail_view, name='chat_detail'),
]