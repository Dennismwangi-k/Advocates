from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = RichTextUploadingField(default ='')
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

