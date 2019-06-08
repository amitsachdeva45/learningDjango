from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from .models import Class
from .forms import ClassForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class MultipleObjectMixing(object):
    def get_object(self,queryset=None,*args,**kwargs):
        slug = self.kwargs.get("slug")
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj = self.get_queryset().first()
            except:
                raise Http404
            return obj
        raise Http404


#DELETE VIEW
class ClassDeleteView(DeleteView):
    model = Class
    template_name = "classBasedView/class_delete.html"
    def get_success_url(self):
        return reverse("class_list")



#UPDATE VIEW
#Update view is using same html file as of create view
#Success url means after saving it will redirect to url having name class_list
#
class ClassUpdateView(MultipleObjectMixing, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "classBasedView/class_create.html"
    def get_success_url(self):
        return reverse("class_list")


#CREATE VIEW
#form_valid is validating a form and apart from title and description
#it is adding data in "added_by" field of form

#In this classcreateview, we are using two different ways of showing message alert
#1) messages.success(self.request, "Created") => This is one way of sending message\
#2) success_message = "%(title)s is created" =>
class ClassCreateView(SuccessMessageMixin, CreateView):
    template_name = "classBasedView/class_create.html"
    form_class = ClassForm
    success_message = "%(title)s is created at %(created_at)s"
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        valid_form = super(ClassCreateView, self).form_valid(form)
        #messages.success(self.request, "Created") => This is one way of sending message
        return valid_form

    def get_success_url(self):
        return reverse("class_list")

    #CUSTOMIZED message
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            created_at = self.object.timestamp,
        )


#LIST VIEW
#Get query Set is showing list and we have used order by (-id)
#which means all ids in descending order
class ClassListView(ListView):
    model = Class

    def get_queryset(self, *args, **kwargs):
        qs = super(ClassListView, self).get_queryset(*args, **kwargs).order_by("-id") #-id means desc order
        #filter(title__startwith = "yet") # we can filter the list of with title having yet
        return qs


#DETAIL VIEW
#Adding a ModelFixingForm in detail view
class ClassDetailView(ModelFormMixin, MultipleObjectMixing, DetailView):
    model = Class
    form_class = ClassForm
    def get_context_data(self, *args, **kwargs):
        context = super(ClassDetailView, self).get_context_data(*args, **kwargs)
        context["form"] = self.get_form() #get_form is function of ModelFormMixing which provide form
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def get_success_url(self):
        return reverse("class_list")



class classBased(TemplateView):
    template_name = "classBasedView/TemplateView.html"
    def get_context_data(self, *args, **kwargs):
        context = super(classBased, self).get_context_data(*args, **kwargs)
        context['title'] = "Template Class View"
        return context


class MyView(ContextMixin, TemplateResponseMixin, View):
    @method_decorator(login_required())
    def get(self,request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "Base Class View"
        return self.render_to_response(context)