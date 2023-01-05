
from core.models import AboutMeModel
from django.core.mail import EmailMessage




def get_email_in_pages(request):
    about_me = AboutMeModel.objects.get(id = 1)
    context = {
        'about_me':about_me
    }
    return context



