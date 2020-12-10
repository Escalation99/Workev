from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from Profile.forms import UserProfileForm
from Discussion.models import Post, Reply
from Profile.models import Profile
from Employee.models import Meeting, Task, Attendance, Notification
from .decorators import unauthenticated_user, allowed_users, HRD_only
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.core.paginator import Paginator


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def index(request):
    template_name = None
    task_qty = Task.objects.filter(given_to=request.user).count()
    recent_post = Post.objects.filter(created_by=request.user)[:2]

    taskFinished = Task.objects.filter(
        given_to=request.user, status="Approved")[:5]
    taskFinishedQty = Task.objects.filter(
        given_to=request.user, status="Approved").count()

    newTask = Task.objects.filter(
        given_to=request.user, status="new")[:5]
    newTaskQty = Task.objects.filter(
        given_to=request.user, status="new").count()

    taskOnProgress = Task.objects.filter(
        given_to=request.user, status="On Progress")[:5]
    taskOnProgressQty = Task.objects.filter(
        given_to=request.user, status="On Progress").count()

    meetings = Meeting.objects.filter(
        division=request.user.profile_user.position)[:5]
    meetings_qty = Meeting.objects.filter(
        division=request.user.profile_user.position).count()

    new_notification = Notification.objects.filter(
        read=False, given_to=request.user).order_by('-created_at')[:2]

    taskUnfinished_qty = task_qty - taskFinishedQty
    employee_qty = User.objects.exclude(username="admin").count()
    clockin_qty = Attendance.objects.exclude(status="Absent").count()
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'recent_post': recent_post,
        'task_qty': task_qty,
        'employee_qty': employee_qty,
        'clockin_qty': clockin_qty,
        'newTask': newTask,
        'taskFinished': taskFinished,
        'taskOnProgress': taskOnProgress,
        'newTaskQty': newTaskQty,
        'taskFinishedQty': taskFinishedQty,
        'taskOnProgressQty': taskOnProgressQty,
        'meetings': meetings,
        'meetings_qty': meetings_qty,
        'new_notification': new_notification,
    }

    if request.user.is_authenticated():
        template_name = 'index_user2.html'
    else:
        template_name = 'index_anonymous.html'

    return render(request, template_name, context)


def registerPage(request):
    if request.method == "POST":
        form1 = UserCreationForm(request.POST)
        form2 = UserProfileForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

            group = Group.objects.get(name="Staff")
            user.groups.add(group)

            username_login = request.POST['username']
            password_login = request.POST['password1']
            user = authenticate(request, username=username_login,
                                password=password_login)
            messages.success(
                request, 'Success creating account!')
            return redirect('index')
        else:
            return redirect('register')
    else:
        form1 = UserCreationForm()
        form2 = UserProfileForm()

    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'register.html', context)


def loginView(request):
    user = None

    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, "login.html")

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')


# @login_required
@allowed_users(allowed_roles=['Staff', 'Admin'])
def logoutView(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
    }
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
        return redirect('/')
    return render(request, "logout.html", context)


def home(request):
    return render(request, 'home.html')
