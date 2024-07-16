from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Page for include new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # Homepage
    path('', views.index, name='index'),
    # Page with all topics
    path('topics/', views.topic, name='topics'),
    # Page with info about theme
    path('topics/<int:topic_id/', views.topic, name='topic'),
]

