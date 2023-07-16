from random import randrange
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from vote.forms import userForm, codeForm, loginForm, bioForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from vote.models import Profile


def index(request):
    return render(request, "vote/index.html")


def login_page(request):
    context = {"form": loginForm, "error": ""}
    return render(request, "vote/login.html", context)


def signUp(request):
    context = {"form": userForm, "confirm_password": ""}

    return render(request, "vote/signUp.html", context)


userDate = []


def authenticate_user(request):
    logout(request)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = userForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                context = {"form": userForm, "error": "This email has been used before"}
                return render(request, "vote/signUp.html", context)
            print(email)
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if password == confirm_password:
                confirmation_code = randrange(1000, 10000)
                send_mail(
                    subject="confirm code ",
                    message="Here is the message:" + str(confirmation_code),
                    from_email="valeriuovidiu1999@gmail.com",
                    recipient_list=[str(email)],
                    fail_silently=False,
                )
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                userDate.append(email)
                userDate.append(password)
                userDate.append(confirmation_code)
                userDate.append(first_name)
                userDate.append(last_name)
                print(userDate)
                context = {"form": codeForm, "error": ""}
                return render(request, "vote/AuthenticationCode.html", context)
        context = {"form": userForm, "error": "Confirm password faild"}

        return render(request, "vote/signUp.html", context)


def create_user(request):
    logout(request)
    if request.method == "POST":
        form = codeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            if code == userDate[2]:
                LastInsertId = (User.objects.last()).id
                user = User.objects.create_user(
                    userDate[3] + " " + userDate[4] + str(LastInsertId + 1),
                    userDate[0],
                    userDate[1],
                )
                user.first_name = userDate[3]
                user.last_name = userDate[4]
                user.save()
                user = authenticate(
                    username=userDate[3] + " " + userDate[4] + str(LastInsertId + 1),
                    password=userDate[1],
                )
                if user is not None:
                    print(user.username)
                    userDate.clear()
                    login(request, user)
                    return redirect("profile")

        context = {"form": codeForm, "error": "introduce the confirmation code again"}
    return render(request, "vote/AuthenticationCode.html", context)


def login_user(request):
    logout(request)
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            try:
                username = User.objects.get(email=email).username
            except:
                context = {"form": loginForm, "error": "Email incorect!"}
                return render(request, "vote/login.html", context)
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("profile")

    context = {"form": loginForm, "error": "Password incorect!"}
    return render(request, "vote/login.html", context)


def post_bio(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = bioForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data["bio"]
            profile = Profile(user=user, bio=bio)
            profile.save()
    return redirect("profile")


def profile(request):
    user = request.user
    run_or_give_up_election = "run for election"
    if hasattr(user, "candidates"):
        run_or_give_up_election = "Give up Election"
    context = {
        "user": user,
        "form": bioForm,
        "bioExists": hasattr(user, "profile"),
        "run_or_give_up_election": run_or_give_up_election,
    }
    return render(request, "vote/profile.html", context)


def logout_views(request):
    logout(request)
    return render(request, "vote/index.html")
