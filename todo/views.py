from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                     password=request.POST['password1'] )
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                      {'form':UserCreationForm(),
                       'error':'Username is taken. Choose another.'})
        else:
            return render(request, 'todo/signupuser.html',
                  {'form':UserCreationForm(), 'error':"Passwords do not match"})

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
