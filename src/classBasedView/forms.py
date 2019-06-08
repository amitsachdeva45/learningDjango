from django import forms
from django.utils.text import slugify
from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = [
            'title',
            'description'
        ]

    #To check if we are entering title should not be duplicate by checking its slug either for update or create class view
    def clean_title(self):
        title = self.cleaned_data['title']
        slug = slugify(title)
        try:
            cl = Class.objects.get(slug = slug)
            raise forms.ValidationError("Title already exist")
        except Class.DoesNotExist:
            return title
        except:
            raise forms.ValidationError("Title already exist")
