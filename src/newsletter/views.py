from django.shortcuts import render
from .forms import SignUpForm, contactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def frontend(request):
    return render(request, "base.html", {})
def contact(request):
    form = contactForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        """
        for key in form.cleaned_data: #Iterate the data of form
            print(key)
            print(form.cleaned_data.get(key))
        """
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        message = form.cleaned_data.get("message")
        print(email, full_name, message)
        subject = message
        from_message = settings.EMAIL_HOST_USER
        to_message = [from_message, "amitsachdeva45@gmail.com"]
        contact_message= "%s : %s via %s"%(email,full_name,message)
        some_html_message = """<h1>Welcome to amit house 3555</h1>"""
        send_mail(
            subject,
            contact_message,
            from_message,
            to_message,
            html_message = some_html_message,
            fail_silently=True)
        #FAIL_silently = It will throw error when it is false
    return render(request,"contact.html",context)



def home(request):
    # {} => Context
    title = "Welcome"

    """
    if request.user.is_authenticated():
        title = "Amit %s" %(request.user) # User who is logged in
    """

    forms  = SignUpForm(request.POST or None)           #Request can be POST when we submit form or just when we call this function
    context = {"template_title" :title, "forms": forms}     #Context should be in dictionary format



    if forms.is_valid():
        instance = forms.save(commit = False)
        if not instance.full_name:
            instance.full_name = 'Amit'
        instance.save()
        context = {"template_title": "Thanks"}                          #If form is submitted, then change context to Thanks

    return render(request, "home.html",context)             # Render combine the combination of data to be shown on html file
