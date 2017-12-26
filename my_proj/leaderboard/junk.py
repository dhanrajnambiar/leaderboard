# def add(request):
#     form_var = participantForm(request.POST or None)#request.POST contains data enterd pertaining to the fields full_name and score
#     list_participants = participant.objects.all()#query set containing all objects in db
#
#     if form_var.is_valid():#to add or delete participant
#         inst_full_name = form_var.clean_full_name()
#         inst_score = form_var.clean_score()
#
#         #if part checks for full_name in db for names and alters scores as edited
#         if list_participants.filter(full_name = inst_full_name).exists():
#             inst_of_dbobj = participant.objects.get(full_name = inst_full_name)
#             inst_of_dbobj.score = inst_score
#             inst_of_dbobj.save()
#         else:
#             form_var.save()
#         return redirect('home')#redirect to 'home' view after adding a participant
#
#     heading = "ADD OR EDIT PARTICIPANT'S"
#     context = {
#             'ranking':list_participants,
#             'form':form_var,
#             'title':heading
#     }
#     return render(request,'leaderboard/add.html',context)
#
# def delete(request):
#     def participants_remaining():
#         list_participants, i = [], 0
#         for item in participant.objects.order_by('-score'):
#             list_participants.append(item.full_name)
#             i += 1
#         return(list_participants)
#
#     if request.method == "POST":
#         name_participant_to_be_deleted = (request.POST.dict()['name_selected'])
#         participant.objects.get(full_name = name_participant_to_be_deleted).delete()
#         names = participants_remaining()
#         return redirect('home')#redirects to 'home' view after deleting a participant
#
#     if request.method == "GET":
#         names = participants_remaining()
#
#     heading = "DELETE PARTICIPANTS"
#     context = {
#         'list':names,
#         'title':heading,
#     }
#
#     return render(request, 'leaderboard/delete.html', context)


# class participantForm(forms.ModelForm):
#     class Meta:
#         model = participant
#         fields = ['full_name','score']#attributes
#
#     def clean_full_name(self):
#         #.cleaned_data() returns a dictionary with the attributes of the participantForm cleaned and the function is mostly defined in the super class of participantForm ie, forms.Model form
#         inst_full_name = self.cleaned_data.get('full_name')
#         return inst_full_name
#
#     def clean_score(self):
#         inst_score = self.cleaned_data.get('score')
#         if inst_score <= 50.00 and inst_score >= 0.00:
#             return inst_score
#         else:
#             raise ValidationError("Please enter a meaningful score between 0 and 50")
