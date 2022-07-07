from django.utils.translation import ugettext

from django.utils.safestring import mark_safe
from django.template import Library

import json


register = Library()


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))

@register.filter(name='template_trans')
def template_trans(text):
    try:
        return ugettext(text)
    except Exception as e:
        return text