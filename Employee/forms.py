from django.forms import ModelForm
from django import forms
from .models import Meeting, Task, TaskReport, ReportFeedback, Attendance, Feedback, FeedbackReply, PaidLeave, TaskReportHistory, SubTask


class DateInput(forms.DateInput):
    input_type = 'date'


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('name', 'type', 'meeting_date', 'meeting_time', 'content', 'room', 'division',
                  'category', 'attachment')

    def clean_meeting(self):
        room = self.cleaned_data.get('room')
        meeting_date = self.cleaned_data.get('meeting_date')

        count = 0
        if self.instance.room == room:
            count += 1
        if self.instance.meeting_date == meeting_date and self.instance.room == room:
            count += 1

        if count == 2:
            raise forms.ValidationError("Meeting already hosted !")
        return meeting_date


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('given_to', 'title', 'body', 'attachment', 'deadline')
        widgets = {
            'deadline': DateInput()
        }


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ('belongs_to', 'title', 'description')


class TaskReportForm(forms.ModelForm):
    class Meta:
        model = TaskReport
        fields = ('comments', 'attachment')


class ReportFeedbackForm(forms.ModelForm):
    class Meta:
        model = ReportFeedback
        fields = ('comments', 'attachment')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('given_to', 'title', 'body')


class FeedbackReplyForm(forms.ModelForm):
    class Meta:
        model = FeedbackReply
        fields = ('title', 'body')


class PaidLeaveForm(forms.ModelForm):
    class Meta:
        model = PaidLeave
        fields = ('title', 'body', 'attachment')
