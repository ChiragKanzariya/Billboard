import datetime
import numpy as np
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.db.models import DurationField, ExpressionWrapper, F
from django.test import TestCase
from pytz import UTC

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
    time_to = forms.CharField(
        widget=forms.TimeInput(attrs={'class': 'timepicker'})
    )
    time_from = forms.CharField(
        widget = forms.TimeInput(attrs={'class': 'timepicker'})
    )
    class Meta:
        model = Post
        fields= ('owner', 'author', 'title', 'clip', 'date_to', 'date_from', 'time_to', 'time_from')


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
    time_to = forms.CharField(
        widget=forms.TimeInput(attrs={'class': 'timepicker'})
    )
    time_from = forms.CharField(
        widget = forms.TimeInput(attrs={'class': 'timepicker'})
    )
    class Meta:
        model = Invitation
        exclude = ('timestamp',)
    
    def clean(self):
        date_to = self.cleaned_data.get('date_to')
        date_from = self.cleaned_data.get('date_from')
        time_to = self.cleaned_data.get('time_to')
        time_from = self.cleaned_data.get('time_from') 
        ori_date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d")
        ori_date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d")
        # ori_time_to = datetime.datetime.strptime(time_to, "%H:%M")
        # ori_time_from = datetime.datetime.strptime(time_from, "%H:%M")

        # dt_array = np.array([ori_date_to + datetime.timedelta(hours=i) for i in range(24)])
        # print(dt_array)
        
        # delta = ori_date_from - ori_date_to
        # my_range = delta.days

        # single_date_to = np.array([ori_date_to + datetime.timedelta(days=i) for i in range(my_range+1)])
        # dt_array = np.array([single_date_to + datetime.timedelta(hours=i) for i in range(24)])
  
        date_to_from_exists = Post.objects.filter(date_to__lte=ori_date_to, date_from__gte=ori_date_from).exists()
        # time_to_from_exists = Post.objects.filter(time_to__lte=ori_time_to, time_from__gte=ori_time_from).exists()
        if date_to_from_exists :
            raise forms.ValidationError("This dates is already booked for billboard")
        super(InvitationForm, self).clean()
        

    
            
