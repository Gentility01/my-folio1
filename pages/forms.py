from django import forms
from core.models import CommentsModel
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import EmailValidator


class CommentForm(forms.ModelForm):
  body = forms.CharField(widget=forms.Textarea(attrs={'rows':1 }))
  
  class Meta:
    model = CommentsModel
    fields = [ 'body']


  
class ContactForm(forms.Form):

    name = forms.CharField(max_length=120 , widget=forms.TextInput(attrs={
        
        'placeholder':' name',
    }))
    email = forms.EmailField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={
        
        'placeholder':'Your Email',
    }))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        
        'placeholder':'Phone',
    }))
    inquiry  = forms.CharField(max_length=70 , widget=forms.TextInput(attrs={
        
        'placeholder':' subject',
    }))
   
    message  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        
        'placeholder':' how can i help you? feel free to get in touch',
        'rows':3
        
    }))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        phone = cl_data.get('phone')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} phone number :{phone} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')
        return subject, msg

    def send(self):

        subject, msg = self.get_info()
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=True
        )
        

    