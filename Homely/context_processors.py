from Employee.models import Notification


def sections_processor(request):
    if request.user.is_authenticated():
        unread_notification = Notification.objects.filter(
            given_to=request.user).count()
        return {'unread_notification': unread_notification}
    else:
        return{'unread_notification': None}
