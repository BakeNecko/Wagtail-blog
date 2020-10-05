from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.routable_page.models import route
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel

from apps.stream_field.blocks import TextBlock
from apps.tutorials.models import BlogListPage
from core.models import BlogBasePage


class AboutPage(BlogBasePage):
    """Home page model."""
    templates = "about_page.html"
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
    banner_angle_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        help_text='Картинка 573х389 на главном header банере',
        blank=False,
        on_delete=models.SET_NULL
    )
    sub_banner_angle_img = models.ForeignKey(
        'wagtailimages.Image',
        related_name='about_sub_banner_angle_img',
        null=True,
        help_text='Мелкаий треугольник возле главного банера',
        blank=False,
        on_delete=models.SET_NULL
    )

    body_block = StreamField([
        ("text", TextBlock()),
    ], null=True, blank=True, editable=True)

    content_panels = Page.content_panels + [
        FieldPanel("heading_title", classname='about_page'),
        FieldPanel('heading_description', classname='about_page'),
        StreamFieldPanel("body_block", classname='about_page'),
        ImageChooserPanel('sub_banner_angle_img', classname='about_page'),
        ImageChooserPanel('banner_angle_img', classname='about_page'),
    ]

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        blog_list = BlogListPage.objects.first()
        return blog_list.category_view(request, cat_slug)

    class Meta:
        verbose_name = "Страница: About"
        verbose_name_plural = "Страница: About"
