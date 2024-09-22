from django.urls import path
from . import views # importa views da pasta learning_logs

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    # Pega um tópico em especifico para ver o seu conteúdo utilizando o id
    path('topics/<topic_id>/', views.topic, name='topic'), 
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
    path('delete_topic/<topic_id>', views.delete_topic, name='delete_topic'),
]
