from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
def signup_view(request):
	if request.method == "POST":
		uname =  request.POST["uname"]
		passwd = request.POST["passwd"]
		user = User.objects.create_user(username=uname,password=passwd)
		user.save()
		return render(request, 'accounts/login.html')
	else:
		return render(request, 'accounts/signup.html')

def login_view(request):
	if request.method == "POST":
			uname =  request.POST["uname"]
			passwd = request.POST["passwd"]
			user = authenticate(request,username=uname,password=passwd)
			if user is not None:
				login(request, user)
				return redirect('articles:list')
			else:
				return render(request, 'accounts/login.html')
	else:
		return render(request, 'accounts/login.html')

def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect('articles:list')
def forgot(request):
	if request.method == "POST":
		global uname
		uname = request.POST["uname"]
		user = User.objects.filter(username=uname)
		print(user)
		if user:
			return redirect('accounts:change_password')
		else:
			return redirect('accounts:login')
	else:
		return render(request,'accounts/forgot.html')
def change_password(request):
	if request.method == "POST":	
		pas=request.POST["passwd"]
		u = User.objects.get(username=uname)
		u.set_password(pas)
		u.save()
		return redirect('accounts:login')
	else:
		return render(request,'accounts/change_password.html')