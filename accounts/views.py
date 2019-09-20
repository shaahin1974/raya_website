from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        # Get from values
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # checks password matches
        if password1 == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'نام کاربری موجود میباشد')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'ایمیل موجود میباشد')
                    return redirect('register')
                else:
                    # look good
                    user = User.objects.create_user(username=username,password=password1,
                                                    email=email)
                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, 'خوش آمدید')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'خوش آمدید لطفا وارد شوید:')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')
