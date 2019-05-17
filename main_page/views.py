from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from .forms import ModelForm
from .forms import ModelForm2
from main_page.breed_detect import detect
from main_page.INFO import information

# Create your views here.
def home(request):
	breeds=''
	
	if request.method == 'POST' and 'predict' in request.POST:
		form=ModelForm(request.POST, request.FILES)
		if form.is_valid():
			
			breeds = detect(form['img1'].value())
			print (breeds)
			
			#print (form['img1'].value())
			#form.save()
			#messages.success(request, f'Thank You!!')
			#return redirect('main_page-home')
	else:
		form=ModelForm()

	if request.method == 'POST' and 'lost' in request.POST:
		form2 = ModelForm2(request.POST, request.FILES)
		if form2.is_valid():
			form2.save()
			return redirect('main_page-lost')
	else:
		form2 = ModelForm2()

	context = {
		'form': form, 
		"breeds": breeds,
		'form2': form2
		
	}
	content = {
	
	}
	return render(request, 'main_page/home.html', context)

def lost(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'main_page/lost.html', context)

def home2(request):
	if request.method == 'POST':
		form=ModelForm2(request.POST, request.FILES)
		
		if form.is_valid():
			#breeds = 'german shepard'
			#print (breed)
			#print (form['img1'].value())
			form.save()
			#messages.success(request, f'Thank You!!')
			return redirect('main_page-lost')
	else:
		form=ModelForm()

	context = {
	'form': form
	}

	return render(request, 'main_page/home2.html', context)
