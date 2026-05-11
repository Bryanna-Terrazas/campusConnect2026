from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserUpdateForm, ProfileUpdateForm, PostingToFeed, TaskForm
from .models import Task, Event, Posts
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from django.contrib.auth.models import User

@login_required
def home(request):
    return render(request, 'home.html', {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect("login")


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {"u_form": u_form, "p_form": p_form})


@login_required
def social(request):
    if request.method == "POST":
        form = PostingToFeed(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("social")
    else:
        form = PostingToFeed()

    posts = Posts.objects.all().order_by('-id')
    return render(request, "social.html", {"s_form": form, "posts": posts})



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks.html', {'tasks': tasks})


from .forms import TaskForm

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created!')
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'task_create.html', {'form': form})


@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_edit.html', {'form': form})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {'task': task})


@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'events.html', {'events': events})


from .forms import EventForm

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event created!')
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'event_create.html', {'form': form})


@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated!')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)

    return render(request, 'event_edit.html', {'form': form})


@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted!')
        return redirect('event_list')

    return render(request, 'event_confirm_delete.html', {'event': event})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Posts, id=post_id, user=request.user)

    if request.method == "POST":
        form = PostingToFeed(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated!")
            return redirect("social")
    else:
        form = PostingToFeed(instance=post)

    return render(request, "post_edit.html", {"form": form})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Posts, id=post_id, user=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted!")
        return redirect("social")

    return render(request, "post_confirm_delete.html", {"post": post})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('login')
    return render(request, 'profile_confirm_delete.html')
    
@login_required
def messages_page(request):
    conversations = Conversation.objects.filter(participants=request.user)
    users = User.objects.all()

    return render(request, "messages.html", {
        "conversations": conversations,
        "users": users
    })

@login_required
def conversation_detail(request, convo_id):
    convo = get_object_or_404(Conversation, id=convo_id)

    if request.method == "POST":
        Message.objects.create(
            conversation=convo,
            sender=request.user,
            body=request.POST.get("body")
        )
        return redirect("conversation_detail", convo_id=convo.id)

    convo_messages = convo.messages.order_by("timestamp")

    return render(request, "conversation.html", {
        "conversation": convo,
        "messages": convo_messages
    })

@login_required
def start_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)

    # prevent chatting with yourself
    if other_user == request.user:
        return redirect("messages")

    # check if conversation already exists
    convo = Conversation.objects.filter(participants=request.user)\
        .filter(participants=other_user)\
        .first()

    # if not, create it
    if not convo:
        convo = Conversation.objects.create()
        convo.participants.add(request.user, other_user)

    return redirect("conversation_detail", convo_id=convo.id)