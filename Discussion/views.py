from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import ReplyForm, PostForm
from .models import Post, Reply
from django.http import HttpResponseRedirect
from Homely.decorators import unauthenticated_user, allowed_users, HRD_only
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import PostFilter


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def index(request):
    post_list = Post.objects.all()

    myFilter = PostFilter(request.GET, queryset=post_list)
    post_list = myFilter.qs

    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'post': post,
        'myFilter': myFilter,
    }

    return render(request, "index.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    replies = Reply.objects.filter(replied_to=post_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    form = ReplyForm(request.POST, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.replied_to = post
            profile.save()
            messages.success(
                request, 'Success creating new reply!')
            return HttpResponseRedirect(request.path_info)

    context = {
        'navbar': is_hrd,
        'post': post,
        'replies': replies,
        'form': form,
    }
    return render(request, "detail.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def indexUser(request):
    post_list = Post.objects.filter(created_by=request.user)
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'post': post,
    }

    return render(request, "indexUser.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def detailUser(request, post_id):
    post = Post.objects.get(id=post_id)
    replies = Reply.objects.filter(replied_to=post_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    form = ReplyForm(request.POST, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.replied_to = post
            profile.save()
            messages.success(
                request, 'Success creating new reply!')
            return HttpResponseRedirect(request.path_info)

    context = {
        'navbar': is_hrd,
        'post': post,
        'replies': replies,
        'form': form,
    }
    return render(request, "detailUser.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def addDiscussion(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.save()
            messages.success(
                request, 'Success creating new post!')
        return redirect('discussion:index')

    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'add_discussion.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def deleteDiscussion(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    post = Post.objects.filter(id=delete_id)
    post.delete()
    messages.success(request, 'Discussion deleted Successfully!')
    return redirect('discussion:indexUser')
    # if request.method == "POST":
    #     if request.POST["confirmRemove"] == "Submit":
    #         post.delete()
    #         messages.success(
    #             request, 'Post Deleted Successfully!')
    #         return redirect('discussion:indexUser')
    #     else:
    #         return redirect('discussion:indexUser')
    # context = {
    #     'navbar': is_hrd,
    #     'post': post,
    # }
    # return render(request, 'removeDiscussionConfirmation.html', context)


def editDiscussion(request, update_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    post = Post.objects.get(id=update_id)
    data = {
        'title': post.title,
        'body': post.body,
        'category': post.category,
        'attachment': post.attachment,
    }
    form = PostForm(request.POST or None, request.FILES or None,
                    initial=data, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Success updating your post!')
            return redirect('discussion:indexUser')
        else:
            messages.error(
                request, 'Failed updating your post!')
            return redirect('discussion:indexUser')

    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'updateDiscussion.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def deleteReplies(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    replies = Reply.objects.filter(id=delete_id)
    replies.delete()
    messages.success(
        request, 'Your Reply Deleted Successfully!')
    return redirect(request.META['HTTP_REFERER'])
