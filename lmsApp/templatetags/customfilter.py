from atexit import register
from django import template
from django.conf import settings


register = template.Library()

@register.filter
def replaceBlank(value,stringVal = ""):
    value = str(value).replace(stringVal, '')
    return value

