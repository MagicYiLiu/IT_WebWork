from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import extendUserData
from .models import userData

# Create your views here.

lst = [
    {'motion': 'Barbell Bench Press', 'motionDone': False},
    {'motion': 'Flat Bench Dumbbell Press', 'motionDone': False},
    {'motion': 'Incline Dumbbell Press  ', 'motionDone': False},
    {'motion': 'Dips For Chest', 'motionDone': True},
]


def home(request):
    # request.POST
    global lst
    if request.method == 'POST':
        if request.POST['motion'] == '':
            content = {'list': lst, 'warning': 'Please enter content！'}
            return render(request, 'myApp/home.html', content)
        else:
            lst.append({'motion': request.POST['motion'], 'motionDone': False})
            content = {'list': lst, 'info': 'Add successful！'}
            return render(request, 'myApp/home.html', content)
    elif request.method == 'GET':
        content = {'list': lst}
        return render(request, 'myApp/home.html', content)


def about(request):
    return render(request, 'myApp/about.html')


def edit(request, forloop_counter):
    global lst
    if request.method == 'POST':
        if request.POST['editDone'] == '':
            return render(request, 'myApp/edit.html', {'warning': 'Please enter content！'})
        else:
            lst[int(forloop_counter) - 1]['motion'] = request.POST['editDone']
            return redirect('myApp:Homepage')

    elif request.method == 'GET':
        content = {'editWait': lst[int(forloop_counter) - 1]['motion']}
        return render(request, 'myApp/edit.html', content)


def delete(request, forloop_counter):
    lst.pop(int(forloop_counter) - 1)
    return redirect('myApp:Homepage')


def cross(request, forloop_counter):
    global lst
    if request.POST['status'] == 'motionDone':
        lst[int(forloop_counter) - 1]['motionDone'] = True
        return redirect('myApp:Homepage')
    elif request.POST['status'] == 'motionNotDone':
        lst[int(forloop_counter) - 1]['motionDone'] = False
        return redirect('myApp:Homepage')


def graphic(request):
    return render(request, 'myApp/graphic.html')


def video(request):
    return render(request, 'myApp//Video/video.html')


# Create Sign in views
def signIn(request):
    if request.method == 'POST':
        users = authenticate(request, username=request.POST['User Name'], password=request.POST['Password'])
        if users is None:
            return render(request, 'myApp/signIn.html', {'Error': 'This User is not exist.'})
        else:
            login(request, users)
            return redirect("myApp:Homepage")
    else:
        return render(request, 'myApp/signIn.html')


def signOut(request):
    logout(request)
    return redirect("myApp:Homepage")


def gotoRegister(request):
    if request.method == 'POST':
        registerForm = extendUserData(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            users = authenticate(username=registerForm.cleaned_data['username'], password=request.POST['password1'])
            userData(users=users, age=registerForm.cleaned_data['age']).save()
            login(request, users)
            return redirect("myApp:Homepage")
    else:
        registerForm = extendUserData()

    content = {'registerForm': registerForm}
    return render(request, 'myApp/register.html', content)


def graphic_31days(request):
    return render(request, 'myApp/graphic/graphic_31days.html')


def graphic_Abs(request):
    return render(request, 'myApp/graphic/graphic_Abs.html')


def graphic_Arms(request):
    return render(request, 'myApp/graphic/graphic_Arms.html')
