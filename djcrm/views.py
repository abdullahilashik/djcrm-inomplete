from django.shortcuts import render, redirect
from django.views import generic

class HomepageView(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_header'] = 'All Leads'
        return context