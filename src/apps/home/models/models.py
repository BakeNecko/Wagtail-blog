from apps.tutorials.models import BlogPostPage, BlogListPage
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from core.models import BlogBasePage
from wagtail.contrib.routable_page.models import route


class HomePage(BlogBasePage):
    """Home page model."""
    templates = "home/home_page.html"
    max_count = 1

    heading_title = models.CharField(
        max_length=140,
        blank=True,
        help_text='Описание главного заголовка Home-Page страницы блога'
    )
    heading_description = models.CharField(
        max_length=255,
        blank=True,
        help_text='Описание верхнего заголовка Home-Page страницы блога'
    )

    content_panels = Page.content_panels + [
        FieldPanel("heading_title", classname='home_page'),
        FieldPanel('heading_description', classname='home_page'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blog_posts = BlogPostPage.objects.all().live().public()
        context["posts"] = blog_posts[:3]
        context["latest_posts"] = blog_posts.last()
        context["tutorials_list_page"] = BlogListPage.objects.first()
        context["most_popular_post"] = blog_posts.first()
        return context

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        blog_list = BlogListPage.objects.first()
        return blog_list.category_view(request, cat_slug)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
