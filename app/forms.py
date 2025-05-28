
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
            'bio': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Enter Bio'}),
            'experience_years': forms.TextInput(attrs={'class': 'my-2 w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Since'}),
            'profile_image': forms.FileInput(attrs={'class': 'my-2 px-4 py-2 border rounded-lg'}),
            'poojas': forms.CheckboxSelectMultiple(attrs={'class': 'my-2 px-4 py-2 border rounded-lg'}),
        }



# class BusinessForm(forms.ModelForm):
#     class Meta:
#         model = Business
#         fields = '__all__'
#         exclude = ['user', 'active','premium','trusted','verified','slug','is_top_in_category','top_rank','views_count']
#         widgets = {
#             'business_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Enter business name'}),
#             'business_description': forms.Textarea(attrs={'class': ' w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300 resize-none', 'rows': 6, 'placeholder': 'Enter business description', 'style': 'width: 100%'}),  # 👈 Full width textarea
#             'business_since': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Since'}),
#             'business_contact': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Enter contact number'}),
#             'business_whatsapp': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Enter WhatsApp number'}),
#             'business_image_1': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'business_image_2': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'business_image_3': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'business_image_4': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'business_image_5': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
#             'business_instagram_link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Instagram link'}),
#             'business_facebook_link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Facebook link'}),
#             'business_youtube_link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'YouTube link'}),
#             'business_x_link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'X (Twitter) link'}),
#             'business_location': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Business location'}),
#             'business_slug': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300', 'placeholder': 'Slug'}),
#             'business_district': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
#             'business_type': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300'}),
#         }

