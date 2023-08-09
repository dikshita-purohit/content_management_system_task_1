from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
	url('signup/', views.signup_view, name = "signup"),
	url('login', views.login_view, name = "login"),
	url('logout', views.logout_view, name = "logout"),
    url('forgot', views.forgot, name = "forgot"),
    url('change_password', views.change_password, name = "change_password"),
]