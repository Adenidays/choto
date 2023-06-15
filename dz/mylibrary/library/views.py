from django.shortcuts import render
from library.models import User


def first_word(request):
    return render(request, 'index.html', context={'users': User.objects.all()})


def show_user(request, author):
    return render(request, 'registr.html', context={'user': User.objects.get(id=author)})
