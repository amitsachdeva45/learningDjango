from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Class(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="book_add")
    last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name="book_edit")
    title = models.CharField(max_length = 120)
    description = models.TextField(null = True, blank = True)
    slug = models.SlugField(unique=True)
    updated  = models.DateTimeField(auto_now_add=False, auto_now= True)
    timestamp = models.DateTimeField(auto_now= False, auto_now_add= True)

    class Meta:
        ordering = ["-timestamp","-id"] #-id means order by id desc. It is default ordering of data in queryset

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse("class_detail",kwargs = {"id":self.id})
        return reverse("class_detail",kwargs = {"slug":self.slug})

def pre_save_class(sender, instance, *args,**kwargs):
    slug = slugify(instance.title)
    instance.slug = slug


# Create your models here.
pre_save.connect(pre_save_class, sender=Class)