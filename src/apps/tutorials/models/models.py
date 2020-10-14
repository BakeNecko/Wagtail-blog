""" Страницы статей Блога. """
from django import forms
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.contrib.routable_page.models import route
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from core.models import BlogBasePage
from apps.stream_field.blocks import TitleBlock, CodeBlock, IMGBlock, TextBlock
from .djagno_models import BlogCategory


class BlogListPage(BlogBasePage):
    template = "posts_list_page.html"
    max_count = 1
    header_title = models.CharField(
        blank=False,
        null=True,
        max_length=155,
        default='Публикации и Посты',
    )
    header_title_description = models.TextField(
        blank=True,
        max_length=500,
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
        related_name='sub_banner_angle_img',
        null=True,
        help_text='Мелкаий треугольник возле главного банера',
        blank=False,
        on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    content_panels = Page.content_panels + [
        FieldPanel("header_title"),
        FieldPanel("header_title_description"),
        ImageChooserPanel('sub_banner_angle_img'),
        ImageChooserPanel('banner_angle_img'),
    ]

    parent_page_types = ['home.HomePage']

    class Meta:
        verbose_name = "Список Постов"
        verbose_name_plural = "Список Постов"

    def get_context(self, request, queryset=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["categories"] = BlogCategory.objects.all()
        context['selected_category'] = None
        context['base_url'] = self.url
        if queryset is None:
            all_posts = BlogPostPage.objects.live().public().order_by('-created_at')
        else:
            all_posts = queryset
        last_post = all_posts.last()
        if last_post is not None:
            all_posts = all_posts.exclude(id=last_post.id)
        paginator = Paginator(all_posts, 9)
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)
        context["blog_post_list"] = posts.object_list
        context['featured_post'] = last_post
        context['posts'] = posts
        context['selected_category'] = None
        return context

    @route(r"^year/(\d+)/(\d+)/$", name="posts_by_year")
    def posts_by_year(self, request, year=None, month=None):
        context = self.get_context(request)
        return render(request, self.template, context)

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        try:
            # Look for the blog category by its slug.
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            # Blog category doesnt exist (ie /blog/category/missing-category/)
            # Redirect to self.url, return a 404.. that's up to you!
            category = None

        if category is None:
            # This is an additional check.
            # If the category is None, do something. Maybe default to a particular category.
            # Or redirect the user to /blog/ ¯\_(ツ)_/¯
            pass
        queryset = BlogPostPage.objects.live().public().filter(categories__in=[category])
        context = self.get_context(request, queryset=queryset)
        context['selected_category'] = category
        # Note: The below template (latest_posts.html) will need to be adjusted
        return render(request, self.template, context)

    def clean(self):
        super().clean()
        # Check Some Fields


class BlogPostPage(BlogBasePage):
    template = "post_page.html"
    categories = ParentalManyToManyField("tutorials.BlogCategory", blank=True)
    post_title = models.CharField(max_length=155, null=True, blank=False, default=None)
    description = models.TextField(
        blank=True,
        max_length=500
    )
    read_length = models.IntegerField(blank=False, null=True, default=15, help_text='Длина чтения статьи')
    blog_preview_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )
    body_block = StreamField([
        ("title", TitleBlock()),
        ("code_block", CodeBlock()),
        ("text", TextBlock()),
        ("img_block", IMGBlock()),
    ], null=True, blank=True, editable=True)

    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    parent_page_types = ['tutorials.BlogListPage']

    content_panels = Page.content_panels + [
        FieldPanel("post_title"),
        FieldPanel("description"),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
        FieldPanel("read_length"),
        ImageChooserPanel("blog_preview_image"),
        StreamFieldPanel("body_block"),
    ]

    class Meta:
        verbose_name = "Страница с постом"
        verbose_name_plural = "Страницы с постами"
        ordering = ['-created_at']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["categories"] = self.categories.all()
        context["tutorials_list_page"] = BlogListPage.objects.first()
        return context

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        blog_list = BlogListPage.objects.first()
        return blog_list.category_view(request, cat_slug)

    def clean(self):
        super().clean()
        # Check Some Fields
        # from django.core.exceptions ValidationError
        # raise ValidationError({
        #   'internal_page': ValidationError("Pleas Select another Url"),
        #   'external_page': ValidationError("Som Error"),
        # }
