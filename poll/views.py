from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Title, Choice, Vote


def index(request):
    if request.user and request.user.is_authenticated:
        poll = Title.objects.all()[0]
        choices = Choice.objects.filter(title=poll)
        context = {'poll': poll, 'choices': choices}
        return render(request, 'poll.html', context=context)
    else:
        return render(request,
                      'login.html')


def register(request):
    if request.method == "POST":
        # register
        pass
    else:
        return redirect('/ffnk')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request,
                          'login.html', {'error': "The provided password is not correct"})

    else:
        return render(request,
                      'login.html')


from django.db.utils import IntegrityError


@transaction.atomic
def vote(request):
    if request.method == 'POST':
        log_out = False
        try:
            party = request.POST.get('vote')
            choice = Choice.objects.get(id=party)
            choice.votes += 1
            choice.save()
            Vote.objects.create(title=choice.title, choice=choice, user=request.user)
            logout(request)
            return render(request,
                          'login.html', {'error': "Thanks for Voting"})
        except IntegrityError:
            return render(request,
                          'login.html', {'error': "You can not vote twice"})
