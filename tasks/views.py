from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):

    if request.method == "GET":
        print("enviando formulario")
        return render(request, 'signup.html', {'form': UserCreationForm()})
    
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    username = request.POST.get('username')
    
    if  password1 != password2:
        return HttpResponse("Passwords do not match")
            
    try:
        #check if username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        
        #create a new user
        user = User.objects.create_user(username=username,password=password1)
        user.save()
        return HttpResponse('User created succesfully')
    except IntegrityError:
        return HttpResponse('Error creating user. Please try again.')
    except Exception as e:
        #Debugging unexpected errors
        print(f"Unexpected error: {e}")
        return HttpResponse("An unexpected error ocurred")
    
    print(request.POST)
    print('obteniendo datos')