from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from Homely.forms import UserCreationForm
from .models import *
from Homely.decorators import unauthenticated_user, allowed_users, HRD_only
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from Discussion.models import Post, Reply
from Profile.models import Profile
from Employee.models import Meeting, Task


# Create your views here.
def index(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    post_qty = Post.objects.filter(created_by=request.user).count()
    reply_qty = Reply.objects.filter(created_by=request.user).count()
    meeting_qty = Meeting.objects.filter(created_by=request.user).count()
    task_qty = Task.objects.filter(created_by=request.user).count()
    finishedTask_qty = Task.objects.filter(
        given_to=request.user, status="Approved").count()
    user = request.user
    context = {
        'navbar': is_hrd,
        'post_qty': post_qty,
        'reply_qty': reply_qty,
        'meeting_qty': meeting_qty,
        'task_qty': task_qty,
        'user': user,
        'finishedTask_qty': finishedTask_qty,
    }
    return render(request, 'profile.html', context)


def updateProfile(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    profile = request.user.profile_user
    data = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': profile.email,
        'address': profile.address,
        'position': profile.position,
        'profile_pic': profile.profile_pic,
    }
    form = UserProfileForm(request.POST, request.FILES,
                           initial=data, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Success updating your profile!')
            return redirect('profile:index')
        else:
            messages.error(
                request, 'Failed updating your profile!')
            return redirect('profile:index')
    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'update_profile.html', context)


def changePassword(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'Success changing password!')
            return redirect('profile:index')
        else:
            messages.error(
                request, 'Change password failed!')
            return redirect('profile:index')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form,
            'navbar': is_hrd,
        }
        return render(request, 'changePassword.html', context)
