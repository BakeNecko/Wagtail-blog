""" Страницы статей Блога. """
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from apps.tutorials.models.djagno_models import BlogCategory


class BlogBasePage(RoutablePageMixin, Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["categories"] = BlogCategory.objects.all()
        context['base_url'] = self.url
        return context

    class Meta:
        abstract = True
