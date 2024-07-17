from django.shortcuts import render, redirect
from django.contrlib.auth import login
from django.contrlib.auth.forms import UserCreationForm


def register(request):
    """register new user"""
    if request.method != 'POST':
        form = UserCreationForm
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'users/register.html', context)

# Create your views here.
