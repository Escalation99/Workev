from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from Homely.decorators import unauthenticated_user, allowed_users, HRD_only
from django.contrib.auth.models import Group, User
from Profile.models import Profile
from django.contrib import messages
from django.core.mail import send_mail
from Employee.models import Meeting, Task, TaskReport, TaskReportHistory, ReportFeedback, Attendance, Feedback, FeedbackReply, Notification, PaidLeave, SubTask
from .forms import MeetingForm, TaskForm, TaskReportForm, ReportFeedbackForm, FeedbackForm, FeedbackReplyForm, PaidLeaveForm, SubTaskForm
import datetime
from django.utils.timezone import utc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import TaskFilter, MeetingFilter, ReportFilter, UserTaskFilter


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def index(request):
    user = User.objects.exclude(username="admin")
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'user': user,
    }

    return render(request, "indexEmployee.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def delete(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    user = User.objects.filter(id=delete_id)
    if request.method == "POST":
        if request.POST["confirmRemove"] == "Submit" and request.POST["confirmationText"] == "CONFIRM":
            user.delete()
            messages.success(
                request, 'User Deleted Successfully!')
            return redirect('employee:index')
        else:
            messages.error(
                request, 'Failed to delete user!')
            return redirect('employee:index')
    context = {
        'navbar': is_hrd,
        'user': user,
    }
    return render(request, 'removeConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def indexSalary(request):
    profile = Profile.objects.exclude(position="CEO")
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'profile': profile,
    }

    return render(request, "indexSalary.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def setSalary(request, user_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    profile = Profile.objects.filter(id=user_id)
    user = User.objects.get(profile_user=profile)

    if request.method == "POST":
        if request.POST["confirmSalary"] == "Submit" and request.POST["salaryAmount"]:
            messages.success(
                request, 'Salary updated successfully!')
            profile.update(salary=request.POST['salaryAmount'])
            notification = Notification(
                created_by=request.user,
                given_to=user,
                title="Salary Update",
                body="Your salary amount have been updated!",
            )
            notification.save()
            return redirect('employee:indexSalary')
        else:
            messages.error(request, 'Salary cannot be empty!')
            return redirect('employee:indexSalary')
    context = {
        'navbar': is_hrd,
        'profile': profile,
    }
    return render(request, 'setSalary.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def sendSalary(request, user_id):
    profile = Profile.objects.filter(id=user_id)
    user = User.objects.get(profile_user=profile)
    send_mail(
        'Monthly Income',
        'Your $1000 monthly income have been sent',
        'raytommy2620@gmail.com',
        ['depape3034@toracw.com'],
        fail_silently=True,
    )
    notification = Notification(
        created_by=request.user,
        given_to=user,
        title="Salary",
        body="Your salary have been sent!",
    )
    notification.save()
    messages.success(
        request, 'Salary sent successfully!')
    return redirect("employee:indexSalary")


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def indexMeeting(request):
    meeting_list = Meeting.objects.order_by('-created_at')

    myFilter = MeetingFilter(request.GET, queryset=meeting_list)
    meeting_list = myFilter.qs

    paginator = Paginator(meeting_list, 10)
    page = request.GET.get('page')
    try:
        meeting = paginator.page(page)
    except PageNotAnInteger:
        meeting = paginator.page(1)
    except EmptyPage:
        meeting = paginator.page(paginator.num_pages)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    form = MeetingForm(request.POST, request.FILES)
    user = User.objects.filter(groups__name='Staff')

    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.save()
            messages.success(
                request, 'Success creating new meeting!')
        else:
            messages.error(request, 'Meeting Room already used in this hour!')
        return redirect('employee:indexMeeting')

    context = {
        'navbar': is_hrd,
        'meeting': meeting,
        'myFilter': myFilter,
        'form': form,
    }

    return render(request, "indexMeeting.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def userMeeting(request):
    meeting1_list = Meeting.objects.filter(
        division=request.user.profile_user.position)
    paginator1 = Paginator(meeting1_list, 5)
    page = request.GET.get('page')
    try:
        meeting1 = paginator1.page(page)
    except PageNotAnInteger:
        meeting1 = paginator1.page(1)
    except EmptyPage:
        meeting1 = paginator1.page(paginator1.num_pages)

    meeting2_list = Meeting.objects.filter(
        division="All")
    paginator2 = Paginator(meeting2_list, 5)
    page = request.GET.get('page')
    try:
        meeting2 = paginator2.page(page)
    except PageNotAnInteger:
        meeting2 = paginator2.page(1)
    except EmptyPage:
        meeting2 = paginator2.page(paginator2.num_pages)

    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'meeting1': meeting1,
        'meeting2': meeting2,

    }

    return render(request, "userMeeting.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteMeeting(request, delete_id):
    meeting = Meeting.objects.filter(id=delete_id)
    meeting.delete()
    messages.success(
        request, 'Meeting deleted Successfully!')
    return redirect('employee:indexMeeting')


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def detailMeeting(request, meeting_id):
    meeting = Meeting.objects.get(id=meeting_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'meeting': meeting,
    }
    return render(request, "detailMeeting.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def detailMeetingUser(request, meeting_id):
    meeting = Meeting.objects.get(id=meeting_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'meeting': meeting,
    }
    return render(request, "detailMeetingUser.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def indexTask(request):

    task_list = Task.objects.order_by('-created_at')

    myFilter = TaskFilter(request.GET, queryset=task_list)

    task_list = myFilter.qs

    paginator = Paginator(task_list, 10)
    page = request.GET.get('page')
    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    form = TaskForm(request.POST, request.FILES)
    form2 = SubTaskForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.save()

            notification = Notification(
                created_by=request.user,
                given_to=profile.given_to,
                title="New Task",
                body="New Task have been uploaded for you!",
            )
            notification.save()

            messages.success(
                request, 'Success creating new task!')
            return redirect('employee:indexTask')

        elif form2.is_valid():
            subtask = SubTask()
            subtask.belongs_to = form2.cleaned_data['belongs_to']
            subtask.title = form2.cleaned_data['title']
            subtask.description = form2.cleaned_data['description']
            subtask.given_to = form2.cleaned_data['belongs_to'].given_to
            subtask.finished = False
            subtask.save()
            messages.success(
                request, 'Success creating new subtask!')
            return redirect('employee:indexTask')
        else:
            messages.error(
                request, 'Error creating new task!')
            return redirect('employee:indexTask')

    context = {
        'navbar': is_hrd,
        'task': task,
        'myFilter1': myFilter,
        'form': form,
        'form2': form2,
    }

    return render(request, "indexTask.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteTask(request, delete_id):
    task = Task.objects.filter(id=delete_id)
    task.delete()
    notification = Notification(
        created_by=request.user,
        given_to=task.given_to,
        title="Task Deleted",
        body="Your Task have been deleted!",
    )
    notification.save()
    messages.success(
        request, 'Task deleted Successfully!')
    return redirect('employee:indexTask')


def editTask(request, update_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    task = Task.objects.get(id=update_id)
    data = {
        'given_to': task.given_to,
        'title': task.title,
        'body': task.body,
        'attachment': task.attachment,
    }
    form = TaskForm(request.POST or None, request.FILES or None,
                    initial=data, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Success updating task!')
            return redirect('employee:indexTask')
        else:
            messages.error(
                request, 'Failed updating task!')
            return redirect('employee:indexTask')
        
        notification = Notification(
                created_by=request.user,
                given_to=task.given_to,
                title="Task Updated",
                body="Your Task have been updated!",
            )
        notification.save()

    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'updateTask.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def detailTask(request, task_id):
    task = Task.objects.get(id=task_id)
    subtask = SubTask.objects.filter(belongs_to=task)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    checkSubtask = SubTask.objects.filter(
        given_to=request.user, finished=False, belongs_to=task.id).count()

    context = {
        'navbar': is_hrd,
        'task': task,
        'subtask': subtask,
        'checkSubtask': checkSubtask,
    }
    return render(request, "detailTask.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def userTask(request):
    task_list = Task.objects.filter(
        given_to=request.user).order_by('-created_at')

    myFilter = UserTaskFilter(request.GET, queryset=task_list)
    task_list = myFilter.qs

    paginator = Paginator(task_list, 10)
    page = request.GET.get('page')
    try:
        task = paginator.page(page)
    except PageNotAnInteger:
        task = paginator.page(1)
    except EmptyPage:
        task = paginator.page(paginator.num_pages)

    task_qty = Task.objects.filter(
        given_to=request.user).count()
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'task': task,
        'task_qty': task_qty,
        'myFilter': myFilter,
    }

    return render(request, "userTask.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def acceptTask(request, task_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        if request.POST["confirmAccept"] == "Submit":
            task.status = "On Progress"
            task.save()
            messages.success(
                request, 'Task accepted successfully!')
            return redirect('employee:userTask')
        else:
            return redirect('employee:userTask')
    context = {
        'navbar': is_hrd,
        'task': task,
    }
    return render(request, 'acceptTaskConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def submitTask(request, task_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    task = Task.objects.get(id=task_id)
    checkSubtask = SubTask.objects.filter(
        given_to=request.user, finished=False, belongs_to=task.id).count()
    form = TaskReportForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.task = task
            profile.created_by = request.user
            profile.given_to = task.created_by
            profile.save()
            task.status = "Waiting Approval"
            task.save()
            messages.success(
                request, 'Success submit task!')
            return redirect('employee:userTask')
        else:
            messages.error(
                request, 'Failed submit task!')
            return redirect('employee:userTask')

    context = {
        'form': form,
        'navbar': is_hrd,
        'task': task,
        'checkSubtask': checkSubtask,
    }
    return render(request, 'submitTask.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def indexReport(request):
    report_list = TaskReport.objects.order_by('-sent_at')
    feedback = ReportFeedback.objects.all()

    myFilter = ReportFilter(request.GET, queryset=report_list)
    report_list = myFilter.qs

    paginator = Paginator(report_list, 10)
    page = request.GET.get('page')
    try:
        report = paginator.page(page)
    except PageNotAnInteger:
        report = paginator.page(1)
    except EmptyPage:
        report = paginator.page(paginator.num_pages)

    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'report': report,
        'myFilter': myFilter,
    }
    return render(request, "indexReport.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def approveReport(request, report_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    report = TaskReport.objects.get(id=report_id)
    task = Task.objects.get(id=report.task.id)
    form = ReportFeedbackForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.report = report
            profile.created_by = request.user
            profile.given_to = report.created_by
            profile.save()

            notification = Notification(
                created_by=request.user,
                given_to=report.created_by,
                title="Task Approval",
                body="Your Task have been approved !",
            )
            notification.save()

            task.status = "Approved"
            task.save()
            messages.success(
                request, 'Success submit report approval!')
            return redirect('employee:indexReport')
        else:
            messages.error(
                request, 'Failed approving report!')
            return redirect('employee:indexReport')

    context = {
        'form': form,
        'navbar': is_hrd,
        'report': report,
        'task': task,
    }
    return render(request, 'submitFeedback.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def rejectReport(request, report_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    report = TaskReport.objects.get(id=report_id)
    task = Task.objects.get(id=report.task.id)
    form = ReportFeedbackForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.report = report
            profile.created_by = request.user
            profile.given_to = report.created_by
            profile.save()

            notification = Notification(
                created_by=request.user,
                given_to=report.created_by,
                title="Task Rejected",
                body="Your Task have been rejected!",
            )
            notification.save()

            task.status = "Rejected"
            task.save()
            messages.success(
                request, 'Success submit report rejection!')
            return redirect('employee:indexReport')
        else:
            messages.error(
                request, 'Failed rejecting report!')
            return redirect('employee:indexReport')

    context = {
        'form': form,
        'navbar': is_hrd,
        'report': report,
        'task': task,
    }
    return render(request, 'submitReject.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def showFeedback(request, task_id):
    task = Task.objects.get(id=task_id)
    report = TaskReport.objects.get(task=task)
    feedback = ReportFeedback.objects.filter(report=report)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'feedback': feedback,
        'task': task,
    }
    return render(request, "showFeedback.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def detailReport(request, report_id):
    report = TaskReport.objects.get(id=report_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'report': report,
    }
    return render(request, "detailReport.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def indexAttendance(request):
    attendance_list = Attendance.objects.all()
    paginator = Paginator(attendance_list, 10)
    page = request.GET.get('page')
    try:
        attendance = paginator.page(page)
    except PageNotAnInteger:
        attendance = paginator.page(1)
    except EmptyPage:
        attendance = paginator.page(paginator.num_pages)

    time = datetime.datetime.utcnow().replace(tzinfo=utc)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'attendance': attendance,
        'time': time,
    }

    return render(request, "indexAttendance.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def clockIn(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    time = datetime.datetime.now()
    context = {
        'navbar': is_hrd,
        'time': time,
    }
    if request.method == "POST":
        if request.POST["clockIn"] == "Submit":
            attendance = Attendance(
                user=request.user,
                status="Present")
            attendance.save()
            messages.success(
                request, 'Successfully Clock In!')
            return redirect('index')
        else:
            messages.error(
                request, 'Failed Clock In!')
            return redirect('index')
    return render(request, 'clockIn.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def clockOut(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    time = datetime.datetime.utcnow().replace(tzinfo=utc)
    context = {
        'navbar': is_hrd,
        'time': time,
    }
    if request.method == "POST":
        if request.POST["clockOut"] == "Submit":
            attendance = Attendance.objects.filter(
                user=request.user).order_by('-id')[0]
            attendance.status = "Finished"
            attendance.save()
            messages.success(
                request, 'Successfully Clock Out!')
            return redirect('index')
        else:
            messages.error(
                request, 'Failed Clock Out!')
            return redirect('index')
    return render(request, 'clockOut.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteAttendance(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    attendance = Attendance.objects.filter(id=delete_id)
    if request.method == "POST":
        if request.POST["confirmRemove"] == "Submit":
            attendance.delete()
            messages.success(
                request, 'Attendance deleted Successfully!')
            return redirect('employee:indexAttendance')
        else:
            return redirect('employee:indexAttendance')
    context = {
        'navbar': is_hrd,
        'attendance': attendance,
    }
    return render(request, 'removeAttendanceConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteReport(request, delete_id):
    report = TaskReport.objects.get(id=delete_id)

    report_history = TaskReportHistory()
    report_history.task = report.task
    report_history.created_by = report.created_by
    report_history.given_to = report.given_to
    report_history.comments = report.comments
    report_history.attachment = report.attachment
    report_history.save()

    report.delete()
    messages.success(
        request, 'Report deleted Successfully!')
    return redirect('employee:indexReport')


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def indexAppFeedback(request):
    feedback_list = Feedback.objects.all()
    paginator = Paginator(feedback_list, 10)
    page = request.GET.get('page')
    try:
        feedback = paginator.page(page)
    except PageNotAnInteger:
        feedback = paginator.page(1)
    except EmptyPage:
        feedback = paginator.page(paginator.num_pages)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'feedback': feedback,
    }

    return render(request, "indexAppFeedback.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def detailAppFeedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'feedback': feedback,
    }
    return render(request, "detailAppFeedback.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def addAppFeedback(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    receiver = User.objects.get(username='admin')
    form = FeedbackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.given_to = receiver
            profile.save()
            messages.success(
                request, 'Success creating new Feedback!')
            return redirect('index')
        else:
            messages.error(
                request, 'Failed creating new Feedback!')
            return redirect('index')

    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'addAppFeedback.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteAppFeedback(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    feedback = Feedback.objects.filter(id=delete_id)
    if request.method == "POST":
        if request.POST["confirmRemove"] == "Submit":
            feedback.delete()
            messages.success(
                request, 'Feedback deleted Successfully!')
            return redirect('employee:indexAppFeedback')
        else:
            return redirect('employee:indexAppFeedback')
    context = {
        'navbar': is_hrd,
        'feedback': feedback,
    }
    return render(request, 'removeFeedbackConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def addAppFeedbackReply(request, feedback_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    feedback = Feedback.objects.get(id=feedback_id)
    form = FeedbackReplyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.given_to = feedback.created_by
            profile.save()

            notification = Notification(
                created_by=request.user,
                given_to=feedback.created_by,
                title="Feedback Reply",
                body="You have a new Feedback Reply",
            )
            notification.save()

            messages.success(
                request, 'Success replying to Feedback!')
            return redirect('index')
        else:
            messages.error(
                request, 'Failed replying to Feedback!')
            return redirect('index')

    context = {
        'form': form,
        'navbar': is_hrd,
        'feedback': feedback,
    }
    return render(request, 'addAppFeedbackReply.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def indexNotification(request):
    notification_list = Notification.objects.order_by('-created_at').filter(
        given_to=request.user)
    notif_qty = Notification.objects.filter(given_to=request.user).count()
    paginator = Paginator(notification_list, 10)
    page = request.GET.get('page')
    try:
        notification = paginator.page(page)
    except PageNotAnInteger:
        notification = paginator.page(1)
    except EmptyPage:
        notification = paginator.page(paginator.num_pages)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'notification': notification,
        'notif_qty': notif_qty,
    }

    return render(request, "indexNotification.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def deleteNotification(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    notification = Notification.objects.filter(id=delete_id)
    notification.delete()
    messages.success(
        request, 'Notification deleted Successfully!')
    return redirect('employee:indexNotification')


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def indexPaidLeave(request):
    paidleave_list = PaidLeave.objects.order_by('-created_at')
    paidleave_qty = PaidLeave.objects.all().count()
    paginator = Paginator(paidleave_list, 10)
    page = request.GET.get('page')
    try:
        paidleave = paginator.page(page)
    except PageNotAnInteger:
        paidleave = paginator.page(1)
    except EmptyPage:
        paidleave = paginator.page(paginator.num_pages)

    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'paidleave': paidleave,
        'paidleave_qty': paidleave_qty,
    }

    return render(request, "indexPaidLeave.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def deletePaidLeave(request, delete_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    paidleave = PaidLeave.objects.filter(id=delete_id)
    if request.method == "POST":
        if request.POST["confirmRemove"] == "Submit":
            paidleave.delete()

            if request.user.username == "admin":
                notification = Notification(
                    created_by=request.user,
                    given_to=paidleave.created_by,
                    title="Paid Leave Rejection",
                    body="Your Paid Leave have been highly rejected !",
                )
                notification.save()

            messages.success(
                request, 'Paid Leave deleted Successfully!')
            return redirect('employee:indexPaidLeave')
        else:
            return redirect('employee:indexPaidLeave')
    context = {
        'navbar': is_hrd,
        'paidleave': paidleave,
    }
    return render(request, 'removePaidLeaveConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff', 'Admin'])
def detailPaidLeave(request, paidleave_id):
    paidleave = PaidLeave.objects.get(id=paidleave_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()

    context = {
        'navbar': is_hrd,
        'paidleave': paidleave,
    }
    return render(request, "detailPaidLeave.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def acceptPaidLeave(request, paidleave_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    paidleave = PaidLeave.objects.get(id=paidleave_id)
    if request.method == "POST":
        if request.POST["confirmPaidLeave"] == "Submit":
            paidleave.status = "Confirmed"
            paidleave.save()

            notification = Notification(
                created_by=request.user,
                given_to=paidleave.created_by,
                title="Paid Leave Approval",
                body="Your Paid Leave have been approved !",
            )
            notification.save()

            messages.success(
                request, 'Paid Leave approved Successfully!')
            return redirect('employee:indexPaidLeave')
        else:
            return redirect('employee:indexPaidLeave')

    context = {
        'navbar': is_hrd,
        'paidleave': paidleave,
    }
    return render(request, 'PaidLeaveConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def rejectPaidLeave(request, paidleave_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    paidleave = PaidLeave.objects.get(id=paidleave_id)
    if request.method == "POST":
        if request.POST["rejectPaidLeave"] == "Submit":
            paidleave.status = "Rejected"
            paidleave.save()

            notification = Notification(
                created_by=request.user,
                given_to=paidleave.created_by,
                title="Paid Leave Rejection",
                body="Your Paid Leave have been rejected !",
            )
            notification.save()

            messages.success(
                request, 'Paid Leave rejected Successfully!')
            return redirect('employee:indexPaidLeave')
        else:
            return redirect('employee:indexPaidLeave')

    context = {
        'navbar': is_hrd,
        'paidleave': paidleave,
    }
    return render(request, 'PaidLeaveRejectionConfirmation.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def addPaidLeave(request):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    receiver = User.objects.get(username='admin')
    form = PaidLeaveForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.created_by = request.user
            profile.given_to = receiver
            profile.save()

            notification = Notification(
                created_by=request.user,
                given_to=profile.given_to,
                title="Paid Leave Request Posted !",
                body="You have uploaded a new Paid Leave Request !",
            )
            notification.save()

            messages.success(
                request, 'Success requesting new Paid Leave !')
            return redirect('index')
        else:
            messages.error(
                request, 'Failed requesting new Paid Leave !')
            return redirect('index')

    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'addPaidLeave.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def userPaidLeave(request):
    paidleave_list = PaidLeave.objects.order_by(
        '-created_at').filter(created_by=request.user)
    paidleave_qty = paidleave_list.count()
    paginator = Paginator(paidleave_list, 10)
    page = request.GET.get('page')
    try:
        paidleave = paginator.page(page)
    except PageNotAnInteger:
        paidleave = paginator.page(1)
    except EmptyPage:
        paidleave = paginator.page(paginator.num_pages)

    is_hrd = request.user.groups.filter(name='Admin').exists()
    context = {
        'navbar': is_hrd,
        'paidleave': paidleave,
        'paidleave_qty': paidleave_qty,
    }

    return render(request, "userPaidLeave.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def finishSubtask(request, subtask_id):
    subtask = SubTask.objects.filter(id=subtask_id)
    subtask.update(finished=True)
    messages.success(
        request, 'Subtask finished Successfully!')
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteSubtask(request, subtask_id):
    subtask = SubTask.objects.get(id=subtask_id)
    subtask.delete()
    messages.success(
        request, 'Subtask deleted Successfully!')
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin', 'Staff'])
def undoSubtask(request, subtask_id):
    subtask = SubTask.objects.filter(id=subtask_id)
    subtask.update(finished=False)
    messages.success(
        request, 'Subtask status have changed Successfully!')
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def editSubtask(request, update_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    subtask = SubTask.objects.get(id=update_id)
    data = {
        'belongs_to': subtask.belongs_to,
        'title': subtask.title,
        'description': subtask.description,
        'finished': subtask.finished,
        'given_to': subtask.given_to,
    }
    form = SubTaskForm(request.POST or None, request.FILES or None,initial=data, instance=subtask)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Success updating subtask!')
            return redirect('employee:indexTask')

        else:
            messages.error(
                request, 'Failed updating subtask!')
            return redirect('employee:indexTask')

    notification = Notification(
                created_by=request.user,
                given_to=subtask.given_to,
                title="Subtask Edited!",
                body="Your subtask have been edited!",
            )
    notification.save()
    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'updateSubtask.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def editMeeting(request, update_id):
    is_hrd = request.user.groups.filter(name='Admin').exists()
    meeting = Meeting.objects.get(id=update_id)
    data = {
        'created_by': meeting.created_by,
        'name': meeting.name,
        'type': meeting.type,
        'content': meeting.content,
        'room': meeting.room,
        'meeting_date': meeting.meeting_date,
        'meeting_time': meeting.meeting_time,
        'category': meeting.category,
        'division': meeting.division,
        'created_at': meeting.created_at,
        'attachment': meeting.attachment,
    }
    form = MeetingForm(request.POST or None, request.FILES or None,initial=data, instance=meeting)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Success updating meeting!')
            return redirect('employee:indexMeeting')

        else:
            messages.error(
                request, 'Failed updating meeting!')
            return redirect('employee:indexMeeting')

    context = {
        'form': form,
        'navbar': is_hrd,
    }
    return render(request, 'updateMeeting.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['Staff'])
def detailNotification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    is_hrd = request.user.groups.filter(name='Admin').exists()
    notification.read = True
    notification.save();

    context = {
        'navbar': is_hrd,
        'notification': notification,
    }
    return render(request, "detailNotification.html", context)
