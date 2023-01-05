
from django.contrib.auth.forms import  UserCreationForm
# from django.contrib.auth.models import User
from user.models import UserModel
from django import forms
from django.forms import ModelForm





class CreateUserForms(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        
        'placeholder':' Username',
    }))
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={
        
        'placeholder':'Your Email',
    }))
    phone = forms.CharField(max_length=50, widget=forms.NumberInput(attrs={
        
        'placeholder':'Phone',
    }))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        
        'placeholder':' Password',
    }))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        
        'placeholder':'Repeat Password',
    }))
    
    class Meta:
        model = UserModel
        fields = ['username', 'email','phone', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Sorry this email already exist')
        return email


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Sorry the two password didnt match')
        elif len(cd['password1']) < 6:
            raise forms.ValidationError('Sorry password must be upto 6 characters')
        return cd['password2']



class ProfileForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['avatar', 'name', 'username', 'email'] 


