from django import forms
from app_first.models import Author

class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'