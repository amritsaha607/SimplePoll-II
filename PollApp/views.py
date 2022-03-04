from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from PollApp.models import Choice, Poll, User, Vote

# Create your views here.


class HomeView(View):

    def get(self, request):
        polls = Poll.objects.all()
        return render(
            request,
            template_name="PollApp/home.html",
            context={
                "polls": polls,
            }
        )


class PollView(View):

    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(
            request,
            template_name="PollApp/poll.html",
            context={
                "poll": poll,
            }
        )

    def post(self, request, poll_id):
        requestData = request.POST

        choice_id = requestData.get('choice_id')

        poll = Poll.objects.get(id=poll_id)
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(
            poll=poll,
            choice=choice,
        )

        poll_results = []
        for choice in poll.choices.all():
            voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
            poll_results.append([choice.name, voteCount])

        return render(
            request,
            template_name="PollApp/poll.html",
            context={
                "poll": poll,
                "success_message": "Voted Successfully",
                "poll_results": poll_results,
            }
        )


class AuthView(View):

    def register(self, request, username, password):
        if User.objects.filter(username=username).exists():
            return "Username already exists"

        user = User.objects.create(username=username, password=password)
        request.session['user_id'] = user.id

        return "ok"

    def login(self, request, username, password):
        if not User.objects.filter(username=username, password=password).exists():
            return "Invalid credentials"

        request.session['user_id'] = User.objects.get(username=username).id

        return "ok"

    def logout(self, request):
        del request.session['user_id']
        return "ok"

    def post(self, request, *args, **kwargs):
        data = request.POST

        mode = data.get('mode')
        username = data.get('username')
        password = hash(data.get('password'))

        if mode == 'register':
            response = self.register(request, username, password)

        elif mode == 'login':
            response = self.login(request, username, password)
    
        elif mode == 'logout':
            self.logout(request)

        else:
            raise Exception(f"Unknown mode found in authorization : {mode}")

        return JsonResponse({"response": response})
