from django.contrib import admin

# Register your models here.
from .forms import ClassForm
from .models import Class

class ClassAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','slug']
    readonly_fields = ['slug','updated','timestamp','added_by','last_edited_by','get_url']

    def get_url(self, obj, *args, **kwargs):
        return str(obj.get_absolute_url())

    form = ClassForm

admin.site.register(Class, ClassAdmin)
