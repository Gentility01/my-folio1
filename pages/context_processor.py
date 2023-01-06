
from core.models import AboutMeModel
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404




def get_email_in_pages(request):
    # about_me = get_object_or_404()
    about_me = AboutMeModel.objects.all()
    context = {
        'about_me':about_me
    }
    return context



