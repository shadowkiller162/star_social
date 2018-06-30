from  django.views.generic import TemplateView

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = "index.html"

class TestPage(TemplateView):
    """docstring fo Test."""
    template_name = "test.html"

class ThanksPage(TemplateView):
    """docstring for ThanksPage."""
    template_name = "thanks.html"
