from django.urls import path, include
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from Produkty.models import Produkty, Kategoria


# Create your views here.

def login_auth(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	kategorie = Kategoria.objects.all()
	return render(request=request, template_name="login.html", context={"login_form":form,'kategorie': kategorie})




def signup_auth(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Rejestracja się udała ! Możesz sie teraz Zarejstrować" )
			return redirect("login")
		messages.error(request, "Coś poszło nie tak. Użytkownik o takim loginie już istnieje lub hasła sie nie zgadzaja")
	form = NewUserForm()
	kategorie = Kategoria.objects.all()
	return render (request=request, template_name="signup.html", context={"register_form":form,'kategorie': kategorie})

def profile(request):
    return render(request, 'profile.html')

def logout_auth(request):
	logout(request)
	messages.success(request, "Zostałeś Wylogowany!") 
	return redirect("/")













