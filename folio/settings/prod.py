from .base import *
import os



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



ALLOWED_HOSTS = ['127.0.0.1', 'my-folio.onrender.com']



DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}






EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
RECIPIENT_ADDRESS= os.environ.get("RECIPIENT_ADDRESS")
EMAIL_USE_TLS = True

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {

    'CLOUD_NAME': os.environ.get("CLOUD_NAME"),
    'API_KEY':os.environ.get("API_KEY"),
    'API_SECRET':os.environ.get("API_SECRET")
}