from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.models import User
from user.forms import SigninForm
# Create your views here.


def signin(request):
    next = request.GET.get('next', '')

    signin_form = SigninForm()
    if request.method != 'POST':
        return render(request, 'signin.html', locals())

    signin_form = SigninForm(request.POST)
    if not signin_form.is_valid():
        login_errors = True
        return render(request, 'signin.html', locals())

    username_or_email = signin_form.cleaned_data['username_or_email']
    password = signin_form.cleaned_data['password']

    key = 'email__iexact' if '@' in username_or_email else 'username__iexact'
    if User.objects.filter(**{key: username_or_email}).exists():
        user = User.objects.get(**{key: username_or_email})
        user = authenticate(username=user.username, password=password)
        if user is None:
            login_errors = True
            return render(request, 'signin.html', locals())
    else:
        login_errors = True
        return render(request, 'signin.html', locals())

    django_login(request, user)

    if next == '':
        next = '/'
    return HttpResponseRedirect(next)