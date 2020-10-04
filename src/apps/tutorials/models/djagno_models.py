""" Страницы статей Блога. """
from django.db import models
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class BlogCategory(models.Model):
    """Blog category for a snippet."""
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", editable=True)

    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name