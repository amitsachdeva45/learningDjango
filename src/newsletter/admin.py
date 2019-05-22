from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp","updated"] #List columms show in listing
    """fields = ['email','timestamp','updated'] #Fiels inside form for admin
    exclude = ['full_name'] #Exclude in Form
    readonly_fields = ['timestamp','updated']
    class Meta:
           model = SignUp"""

    form = SignUpForm



admin.site.register(SignUp,SignUpAdmin) #We are linking our model with Admin


