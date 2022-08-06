from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def signup (request):
    if request.method == 'POST':

        Username = request.POST['Username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Password2 = request.POST['Password2']

        if Password == Password2:
            if User.objects.filter(email=Email).exists():
                messages.info (request, 'Email Taken')
                return redirect ('signup')
            elif User.objects.filter (Username=Username).exists():
                    messages.info (request, 'Username Taken')
                    return redirect ('signup')
            else:
                User = User.objects.create_user(Username=Username, email=Email, Password=Password2)
                User.save()

                #log user in and redirect to settings



                #create a profile object for the new user
                User_model = User.objects.get(Username=Username)
                new_profile = Profile.objects.create(User = User_model, id_user = User_model.id)
                new_profile.save()
                return redirect ('signup')


            else:
            messages.info(request, 'Password Not Matching')
            return redirect ('signup')






    else:
        return render (request, 'signup.html')
