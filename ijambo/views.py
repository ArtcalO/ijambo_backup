from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . forms import *
# Create your views here.

class HomeView(View):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, locals())

def register(request):
	if request.method == "POST" :
		register_form = Registerregister_form(request.POST, request.FILES)
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			first_name = register_form.cleaned_data['first_name']
			last_name = register_form.cleaned_data['last_name']
			password = register_form.cleaned_data['password']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			avatar = register_form.cleaned_data['avatar']
			if password==password2:
				user = User.objects.create_user(
					username=username,
					first_name=first_name,
					last_name=last_name,
					email=email, 
					password=password)
				Profil(user=user, avatar=avatar).save()
		if user:
			login(request, user)
			return redirect(Home)
	register_form = RegisterForm()
	return render(request, 'register.html', locals())