from Employee.models import Notification


def sections_processor(request):
    if request.user.is_authenticated():
        unread_notification = Notification.objects.filter(
            given_to=request.user).count()
        unread_notification2 = Notification.objects.filter(
            given_to=request.user).order_by('-created_at')[:3]
        return {'unread_notification': unread_notification, 'unread_notification2': unread_notification2}
    else:
        return{'unread_notification': None}
