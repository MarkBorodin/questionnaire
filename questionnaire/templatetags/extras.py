from django import template

register = template.Library()


@register.simple_tag
def define(obj):
    return obj
