
import auto_prefetch
from django.db import models
from ckeditor.fields import RichTextField




class TimeBasedModel(auto_prefetch.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta(auto_prefetch.Model.Meta):
        abstract = True




 

class NameBaseModel(TimeBasedModel):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True,blank=True)
    description = RichTextField(null=True)

    
    class Meta(auto_prefetch.Model.Meta):
        abstract = True
        ordering = ["name", "created_at"]

    def __str__(self):
        return self.name

class ExperienceAndSchoolModel(auto_prefetch.Model):
    date_started = models.DateField(null=True, blank=True)
    date_stopped = models.DateField(null=True, blank=True)

    class Meta(auto_prefetch.Model.Meta):
        abstract = True




    

    