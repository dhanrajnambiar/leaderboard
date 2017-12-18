from django import forms
from django.core.exceptions import ValidationError

from .models import participant


class participantForm(forms.ModelForm):
    class Meta:
        model = participant
        fields = ['full_name','score']#attributes

    def clean_full_name(self):
        #.cleaned_data() returns a dictionary with the attributes of the participantForm cleaned and the function is mostly defined in the super class of participantForm ie, forms.Model form
        inst_full_name = self.cleaned_data.get('full_name')
        return inst_full_name

    def clean_score(self):
        inst_score = self.cleaned_data.get('score')
        if inst_score <= 50.00 and inst_score >= 0.00:
            return inst_score
        else:
            raise ValidationError("Please enter a meaningful score between 0 and 50")

# class deleteParticipantForm(forms.Form):
#     def existing_participants():
#         x = participant.objects.order_by('pk')
#         new, slno = [], 1
#         for items in x:
#             new.append((slno,items.full_name))
#             slno += 1
#         return tuple(new)
#
#     select_participant_to_delete = forms.ChoiceField( widget = forms.RadioSelect, choices = existing_participants())
