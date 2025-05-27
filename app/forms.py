
from django import forms
from .models import Review , IyerProfile



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']



class IyerProfileForm(forms.ModelForm):
    class Meta:
        model = IyerProfile
        fields = ['bio', 'experience_years', 'poojas', 'profile_image', 'is_available']
        widgets = {
            'poojas': forms.CheckboxSelectMultiple(),
        }



