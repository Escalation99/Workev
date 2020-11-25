from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^generatePerformance/(?P<profile_id>[0-9]+)/$',
        views.generatePerformance, name="generatePerformance",),
    url(r'^indexPerformance/$', views.indexPerformance, name="indexPerformance"),

    url(r'^editSubtask/(?P<update_id>[0-9]+)$',
        views.editSubtask, name="editSubtask"),
    url(r'^deleteSubtask/(?P<subtask_id>[0-9]+)$',
        views.deleteSubtask, name="deleteSubtask"),
    url(r'^finishSubtask/(?P<subtask_id>[0-9]+)$',
        views.finishSubtask, name="finishSubtask"),
    url(r'^undoSubtask/(?P<subtask_id>[0-9]+)$',
        views.undoSubtask, name="undoSubtask"),

    url(r'^userPaidLeave/$', views.userPaidLeave, name="userPaidLeave"),
    url(r'^addPaidLeave/$', views.addPaidLeave, name="addPaidLeave"),
    url(r'^rejectPaidLeave/(?P<paidleave_id>[0-9]+)/$',
        views.rejectPaidLeave, name="rejectPaidLeave",),
    url(r'^acceptPaidLeave/(?P<paidleave_id>[0-9]+)/$',
        views.acceptPaidLeave, name="acceptPaidLeave",),
    url(r'^detailPaidLeave/(?P<paidleave_id>[0-9]+)/$',
        views.detailPaidLeave, name="detailPaidLeave",),
    url(r'^deletePaidLeave/(?P<delete_id>[0-9]+)$',
        views.deletePaidLeave, name="deletePaidLeave"),
    url(r'^indexPaidLeave/$', views.indexPaidLeave, name="indexPaidLeave"),

    url(r'^deleteNotification/(?P<delete_id>[0-9]+)$',
        views.deleteNotification, name="deleteNotification"),
    url(r'^indexNotification/$', views.indexNotification, name="indexNotification"),

    url(r'^deleteFeedbackReply/(?P<delete_id>[0-9]+)$',
        views.deleteFeedbackReply, name="deleteFeedbackReply"),
    url(r'^indexFeedbackReply/$', views.indexFeedbackReply,
        name="indexFeedbackReply"),
    url(r'^deleteAppFeedback/(?P<delete_id>[0-9]+)$',
        views.deleteAppFeedback, name="deleteAppFeedback"),
    url(r'^addAppFeedbackReply/(?P<feedback_id>[0-9]+)$', views.addAppFeedbackReply,
        name="addAppFeedbackReply"),
    url(r'^addAppFeedback/$', views.addAppFeedback, name="addAppFeedback"),
    url(r'^detailAppFeedback/(?P<feedback_id>[0-9]+)/$',
        views.detailAppFeedback, name="detailAppFeedback",),
    url(r'^indexAppFeedback/$', views.indexAppFeedback, name="indexAppFeedback"),

    url(r'^deleteAttendance/(?P<delete_id>[0-9]+)$',
        views.deleteAttendance, name="deleteAttendance"),
    url(r'^clockOut/$', views.clockOut, name="clockOut"),
    url(r'^clockIn/$', views.clockIn, name="clockIn"),
    url(r'^indexAttendance/$', views.indexAttendance, name="indexAttendance"),

    url(r'^showFeedback/(?P<task_id>[0-9]+)/$',
        views.showFeedback, name="showFeedback",),

    url(r'^deleteReport/(?P<delete_id>[0-9]+)$',
        views.deleteReport, name="deleteReport"),
    url(r'^detailReport/(?P<report_id>[0-9]+)/$',
        views.detailReport, name="detailReport",),
    url(r'^rejectReport/(?P<report_id>[0-9]+)/$',
        views.rejectReport, name="rejectReport",),
    url(r'^approveReport/(?P<report_id>[0-9]+)/$',
        views.approveReport, name="approveReport",),
    url(r'^indexReport/$', views.indexReport, name="indexReport"),

    url(r'^submitTask/(?P<task_id>[0-9]+)/$',
        views.submitTask, name="submitTask",),
    url(r'^reattemptTask/(?P<task_id>[0-9]+)/$',
        views.reattemptTask, name="reattemptTask",),
    url(r'^acceptTask/(?P<task_id>[0-9]+)/$',
        views.acceptTask, name="acceptTask",),
    url(r'^userTask/$', views.userTask, name="userTask"),

    url(r'^detailTask/(?P<task_id>[0-9]+)/$',
        views.detailTask, name="detailTask",),
    url(r'^editTask/(?P<update_id>[0-9]+)$',
        views.editTask, name="editTask"),
    url(r'^deleteTask/(?P<delete_id>[0-9]+)$',
        views.deleteTask, name="deleteTask"),
    url(r'^indexTask/$', views.indexTask, name="indexTask"),

    url(r'^editMeeting/(?P<update_id>[0-9]+)$',
        views.editMeeting, name="editMeeting"),
    url(r'^finishMeeting/(?P<delete_id>[0-9]+)$',
        views.finishMeeting, name="finishMeeting"),
    url(r'^detailMeetingUser/(?P<meeting_id>[0-9]+)/$',
        views.detailMeetingUser, name="detailMeetingUser",),
    url(r'^detailMeeting/(?P<meeting_id>[0-9]+)/$',
        views.detailMeeting, name="detailMeeting",),
    url(r'^userMeeting/$', views.userMeeting, name="userMeeting"),
    url(r'^indexMeeting/$', views.indexMeeting, name="indexMeeting"),

    url(r'^salary/$', views.indexSalary, name="indexSalary"),
    url(r'^sendSalary/(?P<user_id>[0-9]+)$',
        views.sendSalary, name="sendSalary"),
    url(r'^setSalary/(?P<user_id>[0-9]+)$', views.setSalary, name="setSalary"),

    url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name="delete"),
    url(r'^$', views.index, name="index"),
]
