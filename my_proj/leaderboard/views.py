from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .models import participant,administrator

from .forms import participantForm, UserRegForm, loginForm

# Create your views here.

def home(request):
    sorted_list = participant.objects.order_by('-score');
    heading = "LIST OF TOPPER'S"
    context = {
        'ranking':sorted_list,
        'title':heading
    }

    return render(request, 'leaderboard/home.html', context)

def user_login(request):
    form_var = loginForm(request.POST or None)
    heading = "LOGIN"
    pwd_flag = False#set true if wrong passsword entered
    if request.method == "POST":
        if form_var.is_valid():
            usr_name = form_var.clean_username()
            pwd = form_var.clean_password()
            usr = authenticate(username = usr_name, password = pwd)
            if usr is not None:
                    login(request, usr)
                    return redirect('user_home', username = usr_name)
            else:
                #print("inputted wrong password")
                pwd_flag = True

    if pwd_flag:
        alert_msg = "Username or Password is Incorrect.Please enter correct login details!!!"
    else:
        alert_msg = ""

    context = {
        'msg':alert_msg,
        'form':form_var,
        'title':heading,
    }

    return render(request, 'leaderboard/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def register(request):
    r_form = UserRegForm(request.POST or None)
    heading = "Register Here"
    if request.method == "POST":
        if r_form.is_valid():
            r_form.save(commit = False)
            usrnm = r_form.cleaned_data.get('username')
            pwd1 = r_form.cleaned_data.get('password1')
            mail = r_form.cleaned_data.get('email')
            User.objects.create_user(username = usrnm, password = pwd1, email = mail)
            user_to_login = authenticate(username = usrnm, password = pwd1)
            if user_to_login is not None:
                login(request, user_to_login)
                return redirect('user_home', username = usrnm)

    context = {
        'form':r_form,
        "title":heading,
    }

    return render(request, 'leaderboard/register.html', context)

def user_home(request, username):
    if request.user.is_authenticated and request.user.username == username:
        heading = "Welcome, " + str(username)

        x = User.objects.get(username = username)
        a = administrator.objects.get(user = x)
        list_participants = participant.objects.filter(creator = a).order_by('-score')

        context = {
            'list_participants':list_participants,
            'title':heading,
        }

    else:
        return redirect('user_login')

    return render(request, 'leaderboard/user.html', context)


def add_participant(request, username):
    form_var = participantForm(request.POST or None)#request.POST contains data enterd pertaining to the fields full_name and score

    x = User.objects.get(username = username)
    a = administrator.objects.get(user = x)
    list_participants = participant.objects.filter(creator = a).order_by('-score')#query set containing all objects in db

    if request.user.is_authenticated:
        if form_var.is_valid():#to add or delete participant
            inst_full_name = form_var.clean_full_name()
            inst_score = form_var.clean_score()

            #if part checks for full_name in db for names and alters scores as edited
            if list_participants.filter(full_name = inst_full_name).exists():
                inst_of_dbobj = participant.objects.get(full_name = inst_full_name)
                inst_of_dbobj.score = inst_score
                inst_of_dbobj.save()
            else:
                participant.objects.create(creator = a, full_name = inst_full_name, score = inst_score)
            return redirect('user_home', username)#redirect to 'home' view after adding a participant
    else:
        return redirect('user_login')

    heading = "ADD OR EDIT PARTICIPANT'S"
    context = {
            'ranking':list_participants,
            'form':form_var,
            'title':heading
    }
    return render(request,'leaderboard/add.html',context)

def delete_participant(request, username):
    def participants_remaining():
        x = User.objects.get(username = username)
        a = administrator.objects.get(user = x)
        list_participants, i = [], 0
        for item in participant.objects.filter(creator = a).order_by('-score'):
            list_participants.append(item.full_name)
            i += 1
        return(list_participants)
    if request.user.is_authenticated:
        if request.method == "POST":
            name_participant_to_be_deleted = (request.POST.dict()['name_selected'])
            participant.objects.get(full_name = name_participant_to_be_deleted).delete()
            names = participants_remaining()
            return redirect('user_home', username)#redirects to 'home' view after deleting a participant

        if request.method == "GET":
            names = participants_remaining()

        heading = "DELETE PARTICIPANTS"
        context = {
            'list':names,
            'title':heading,
        }
    else:
        return redirect('user_login')

    return render(request, 'leaderboard/delete.html', context)
