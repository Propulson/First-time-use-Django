from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    """Homepage our app"""
    return render(request, 'learning_logs/index.html')


def topic(request, topic_id):
    """Show list themes"""
    topics = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """show new theme"""
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """include new acc"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect(request, 'learning_log:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log/new_entry.html', context)
