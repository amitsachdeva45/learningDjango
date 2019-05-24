from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.views.generic import View
from django.utils.decorators import method_decorator
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