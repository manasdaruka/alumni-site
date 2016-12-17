from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.conf import settings


def base_response(request, body, title=None, h1=None):
    context_dict = {"base_body": body}
    if title:
        context_dict["base_title"] = title
    if h1:
        context_dict["base_h1"] = h1
    return render(request, "accounts/base.html", context_dict)


def login_view(request):
    context_dict = {}
    if request.method == "POST":
        next_url = ""
        if "next" in request.POST:
            next_url = request.POST["next"]
        if next_url:
            context_dict["next"] = next_url
        if "username" in request.POST and "password" in request.POST and request.POST["username"] and request.POST[
            "password"]:
            username = request.POST["username"]
            password = request.POST["password"]
            context_dict["username"] = username
            user = authenticate(username=username, password=password)
            if not user:
                context_dict["login_error"] = "Username or password is incorrect"
            elif not user.is_active:
                context_dict["login_error"] = "Your account has been disabled. Contact support."
            else:
                login(request, user)
                if not next_url:
                    next_url = settings.LOGIN_REDIRECT_URL
                return HttpResponseRedirect(next_url)
        else:
            context_dict["login_error"] = "You must enter both username and password"
    elif request.method == "GET":
        if "next" in request.GET and request.GET["next"]:
            context_dict["next"] = request.GET["next"]
    return render(request, "accounts/login.html", context_dict)


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    else:
        return base_response(request, "You are already logged out")


def register(request):
    context_dict = {}
    if request.method == "POST":
        keys = ("username", "firstname", "lastname", "password1", "password2")
        if all((key in request.POST and request.POST[key]) for key in keys):
            username = request.POST["username"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            context_dict["username"] = username
            if password1 != password2:
                context_dict["register_error"] = "Passwords do not match"
            elif User.objects.filter(username=username).count() > 0:
                context_dict["register_error"] = "A user with this username already exists"
            else:
                user = User(username=username)
                user.set_password(password1)
                user.first_name = request.POST['firstname']
                user.last_name = request.POST['lastname']
                user.save()
                user = authenticate(username=username, password=password1)
                login(request, user)
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context_dict["register_error"] = "You must fill out all fields"
    return render(request, "accounts/register.html", context_dict)


@login_required
def account_info(request):
    return render(request, "accounts/account_info.html", {})


def edit_profile(request):
    context_dict = {}
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            context_dict["ep_success"] = "Profile changed successsfully"
        else:
            context_dict["ep_error"] = "Invalid data received"
    else:
        form = EditProfileForm(instance=request.user)
    context_dict["form"] = form
    return render(request, "accounts/edit_profile.html", context_dict)
