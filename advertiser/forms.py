import datetime
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from advertiser.models import Post, Invitation

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PostForm(ModelForm):
    title = forms.CharField(
        label = "Title",
        max_length = 100,
        required = True,
    )
    date_to = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}), 
    )
    date_from = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}), 
    )
    class Meta:
        model = Post
        fields= ('owner', 'author', 'title', 'clip', 'date_to', 'date_from')


class InvitationForm(ModelForm):
    title = forms.CharField(
        label = "Title",
        max_length = 100,
        required = True,
    )
    date_to = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}), 
    )
    date_from = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}), 
    )

    class Meta:
        model = Invitation
        exclude = ('timestamp',)
    
    def clean(self):
        date_to = self.cleaned_data.get('date_to')
        date_from = self.cleaned_data.get('date_from') 
        ori_date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
        ori_date_from = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
        date_to_from_exists = Post.objects.filter(date_to__lte=ori_date_to, date_from__gte=ori_date_from).exists()
        if date_to_from_exists:
            raise forms.ValidationError("This dates is already booked for billboard")
        super(InvitationForm, self).clean()
        