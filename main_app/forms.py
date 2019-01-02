from django import forms
# Add this line...
from .models import Cat
# Change the line below to use ModelForm...
class CatForm(forms.ModelForm):
		# Replace the contents with these lines...
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'description', 'age']


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())