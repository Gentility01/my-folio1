from django.db import models
from django.contrib.auth.models import AbstractUser
from folio.utils.media import MediaHelper
# Create your models here.

class UserModel(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255)
    avatar = models.ImageField( upload_to=MediaHelper.get_image_upload_path, null=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
