from django.db import models
import auto_prefetch
from django_resized import ResizedImageField
from folio.utils.media import MediaHelper
from folio.utils.choices import PortfolioChoices
from folio.utils.models import  NameBaseModel, ExperienceAndSchoolModel
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.html import mark_safe
from user.models import UserModel

# Create your models here.

class Experiences(ExperienceAndSchoolModel):
    name_of_place = models.CharField(max_length=200 )
    work_as = models.CharField(max_length=200 )

    class Meta:
        verbose_name = 'Exprience'
        verbose_name_plural = 'Experiences'

class Schools(ExperienceAndSchoolModel):
    name_of_school = models.CharField(max_length=200 )
    course = models.CharField(max_length=200 )
    place = models.CharField(max_length=200 )

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

class AboutMeModel(NameBaseModel):

    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True)
    thumbnail = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image")
    resume_photo = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image", null=True, blank=True)


class ServicesModel(NameBaseModel):
    i_class = models.CharField(max_length=200)
    description2 = models.TextField(null=True)
    image = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('servicedetail',kwargs={'slug':self.slug})
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceRatingModel(NameBaseModel):
    pesentage = models.IntegerField()


class NewsModel(NameBaseModel):
    thumbnail = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image")

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Tags(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Images(models.Model):
    files = models.FileField(upload_to=MediaHelper.get_image_upload_path)
    potfolio = auto_prefetch.ForeignKey( "PotfolioModel", on_delete=models.CASCADE, null=True, blank=True)
    news = auto_prefetch.ForeignKey( NewsModel, on_delete=models.CASCADE,  null=True, blank=True)
    blogs = auto_prefetch.ForeignKey( 'PortfolioBlogModel', on_delete=models.CASCADE,  null=True, blank=True)
    
    def image_tag(self):
        return mark_safe('<img src="MediaHelper.get_image_upload_path%s" width="50" height="50" />'%(self.files))
        # return u'<img src="%s" />' % escape(MediaHelper.get_image_upload_path)
    image_tag.short_description = 'Image'

    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

   


class PotfolioModel(NameBaseModel):
    client = models.CharField(max_length=200)
    firm_name = models.CharField(max_length=200)
    image = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image", null=True, blank=True)
    category = TaggableManager()
    potfoliochoices = models.CharField(choices=PortfolioChoices.choices, max_length=20, default=PortfolioChoices.Backend)
    live_website = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)

    def get_potfolio_url(self):
        return reverse('servicedetail',kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

class PotfolioQuestionModel(models.Model):
    questions = models.CharField(max_length=200, null=True)
    answer = RichTextField(null=True)

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name


class PortfolioBlogModel(NameBaseModel):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image", null=True, blank=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



class CommentsModel(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(PortfolioBlogModel,  on_delete=models.CASCADE) 
    body = models.TextField(help_text='Add a comment') 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'







