from django.shortcuts import render
from django.views.generic import CreateView
from .forms import JoinNewsLetterForm

# Create your views here.
class NewsletterSubscribe(CreateView):
    template_name = 'footer.html'
    form_class = JoinNewsLetterForm
    success_url = '/'

    def validate_form(self, form):
        email = form.cleaned_data.get('email')
        return super(NewsletterSubscribe, self).validate_form(form)