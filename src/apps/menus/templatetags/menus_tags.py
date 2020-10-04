from django import template
from apps.home.models import HomePage
from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.filter(slug=slug).first()


@register.simple_tag()
def get_first_menu():
    return Menu.objects.first()


@register.simple_tag()
def home_page_url():
    return HomePage.objects.first().url
