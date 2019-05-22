from django import forms

from .models import SignUp

class contactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    def clean_email(self):
        print(self.cleaned_data.get("email")) #Get particular field
        print(self.cleaned_data)
        email = self.cleaned_data.get("email")

        #1) Way to check
        username, provider = email.split("@")
        company, domain = provider.split(".")
        if domain != "edu":
            raise forms.ValidationError("Please use valid .edu school email address")



        """ #2) Way of check if email has .edu at end
        if not ".edu" in email:
            raise forms.ValidationError("Please use valid .edu school email address")
        """


        return email #Replace the value of email field by amitsachdeva45@gmail.com (Cleaning data)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name","email"]

    def clean_email(self):
        print(self.cleaned_data.get("email")) #Get particular field
        print(self.cleaned_data)
        email = self.cleaned_data.get("email")

        #1) Way to check
        username, provider = email.split("@")
        company, domain = provider.split(".")
        if domain != "edu":
            raise forms.ValidationError("Please use valid .edu school email address")



        """ #2) Way of check if email has .edu at end
        if not ".edu" in email:
            raise forms.ValidationError("Please use valid .edu school email address")
        """


        return email #Replace the value of email field by amitsachdeva45@gmail.com (Cleaning data)

    def clean_full_name(self): # You must need to maintain naming conventions
        full_name = self.cleaned_data.get("full_name")
        return full_name

