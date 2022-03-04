from PollApp.models import User


def get_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        return User.objects.get(id=user_id)
