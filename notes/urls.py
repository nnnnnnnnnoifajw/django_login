from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),            # 公開フィード
    path('me/', views.note_list_me, name='note_list_me'),   # 自分のノート
    path('new/', views.note_new, name='note_new'),
    path('<int:note_id>/delete/', views.note_delete, name='note_delete'),
]
