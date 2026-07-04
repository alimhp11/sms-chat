from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import Room, Message
from .forms import RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('lobby')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lobby')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def lobby(request):
    rooms = Room.objects.all().order_by('-created_at')
    return render(request, 'lobby.html', {'rooms': rooms})


@login_required
def room(request, room_name):
    room_obj, _ = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room_obj).select_related('user')[:50]
    return render(request, 'room.html', {
        'room_name': room_name,
        'messages': messages,
        'username': request.user.username,
    })


@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip().replace(' ', '_')
        if name:
            Room.objects.get_or_create(name=name)
            return redirect('room',room_name=name)
    return redirect('lobby')



