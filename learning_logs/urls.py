from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page with all topics
    path('topics/', views.topic, name='topics'),
    # Page with info about theme
    path('topics/<int:topic_id/', views.topic, name='topic'),
    # Page for new comments
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for include new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for change entries
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]



