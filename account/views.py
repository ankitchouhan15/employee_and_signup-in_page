from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "signup.html")


def signin(request):
    return render(request, "signin.html")


# def basenav(request):
#     return render(request, "basenav.html")

# for refrence check screenshots
def signuppage(request):
    if request.method == "POST":
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        email = request.POST["email"]
        unm = request.POST["username"]
        pwd = request.POST["password"]
        try:
            user = User.objects.get(username=unm)
            return render(request, "signin.html")
        except:
            user = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                email=email,
                username=unm,
                password=pwd,
            )
            user.save()
            return render(request, "signin.html")
    else:
        return render(request, "signup.html")


def signinpage(request):
    if request.method == "POST":
        email = request.POST["email"]
        pwd = request.POST["password"]
        unm = User.objects.get(email=email.lower()).username
        user = auth.authenticate(username=unm, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("signinsuccess_logout")
        else:
            return render(request, "signin.html")
    else:
        return render(request, "signin.html")


def signinsuccess_logout(request):
    return render(request, "signinsuccess_logout.html")


def logout(request):
    auth.logout(request)
    return render(request, "signin.html")
