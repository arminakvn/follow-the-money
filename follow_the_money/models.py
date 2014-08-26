from django.db import models
# import User model
from django.contrib.auth.models import User
# importing django-taggit
from taggit.managers import TaggableManager


# Create your models here.
# Model that stores Media Images
class MediaImage(models.Model):
    # Links MediaImage to a User model instance.
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="img/%Y_%m_%d_%h_%M_%s", null=False, blank=False)
    caption = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
    tags = TaggableManager()
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
        
# Model that stores Media Audio
class MediaAudio(models.Model):
    # Links MediaAudio to a User model instance.
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, null=False, blank=False)
    audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s", null=False, blank=False)
    caption = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
    tags = TaggableManager()
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
        
# Model that stores Media Notes
class MediaNote(models.Model):
    # Links MediaAudio to a User model instance.
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, null=False, blank=False)
    notes = models.CharField(max_length=2000, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
    tags = TaggableManager()
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
        
# Model that stores Media Images
class MediaInterview(models.Model):
    # Links MediaInterview to a User model instance.
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="img/%Y_%m_%d_%h_%M_%s", null=False, blank=False)
    audio = models.FileField(upload_to="audio/%Y_%m_%d_%h_%M_%s", null=False, blank=False)
    caption = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
    tags = TaggableManager()
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
        
