from django import forms
from . import models

class userForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(userForm, self).__init__(*args, **kwargs)
        for item in userForm.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'

    """
    Email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control','id':'poo'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    """
    class Meta:
        model = models.User
        fields = "__all__"


