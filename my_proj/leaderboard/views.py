from django.shortcuts import render

from .models import participant
from .forms import participantForm# deleteParticipantForm

# Create your views here.

def home(request):
    sorted_list = participant.objects.order_by('-score');
    heading = "LIST OF TOPPER'S"
    context = {
        'ranking':sorted_list,
        'title':heading
    }

    return render(request, 'leaderboard/home.html', context)

def add(request):
    form_var = participantForm(request.POST or None)#request.POST contains data enterd pertaining to the fields full_name and score
    list_participants = participant.objects.all()#query set containing all objects in db
    if form_var.is_valid():
        inst_full_name = form_var.clean_full_name()
        inst_score = form_var.clean_score()

        #if part checks for full_name in db for names and alters scores as edited
        if list_participants.filter(full_name = inst_full_name).exists():
            inst_of_dbobj = participant.objects.get(full_name = inst_full_name)
            inst_of_dbobj.score = inst_score
            inst_of_dbobj.save()
        else:
            form_var.save()
    heading = "ADD OR EDIT PARTICIPANT'S"
    context = {
        'ranking':list_participants,
        'form':form_var,
        'title':heading
    }

    return render(request,'leaderboard/add.html',context)

def delete(request):
    def participants_remaining():
        list_participants, i = [], 0
        for item in participant.objects.order_by('-score'):
            list_participants.append(item.full_name)
            i += 1
        return(list_participants)

    if request.method == "POST":
        name_participant_to_be_deleted = (request.POST.dict()['name_selected'])
        participant.objects.get(full_name = name_participant_to_be_deleted).delete()
        names = participants_remaining()

    if request.method == "GET":
        names = participants_remaining()

    heading = "DELETE PARTICIPANTS"
    context = {
        'list':names,
        'title':heading,
    }

    return render(request, 'leaderboard/delete.html', context)
