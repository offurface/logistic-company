from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(), name='dispatch')
class HomeView(TemplateView):
    template_name = "index.html"

@method_decorator(login_required(login_url='/lol/'), name='dispatch')
class PageLoaderView(TemplateView):
    def dispatch(self, request, template, *args, **kwargs):
        try:
            self.template_name = f'pages/{template}.html'
            get_template(self.template_name)
            return super().dispatch(request, *args, **kwargs)
        except TemplateDoesNotExist:
            raise Http404
