import json

from django import template
from webpack_loader.utils import get_as_tags
from django.utils.safestring import mark_safe
from webpack_loader.exceptions import WebpackBundleLookupError
import re
from django import template
from django.conf import settings

from ..template import EvaluateNode

register = template.Library()


@register.simple_tag
def get_langs_json(langs):
    result = dict()
    for lang in langs:
        result[lang[0]] = lang[1]
    return json.dumps(result)


@register.simple_tag
def vardump(var):
    return vars(var)



@register.simple_tag
def dirdump(var):
    return dir(var)


@register.simple_tag
def define(val=None):
    return val


@register.tag(name="evaluate_template")
def evaluate_template(parser, token):
    """
    tag usage {% evaluate object.textfield %}
    """
    return EvaluateNode(token.split_contents()[1])


@register.simple_tag
def render_bundle(bundle_name, extension=None, config='DEFAULT', attrs=''):
    try:
        tags = get_as_tags(
            bundle_name,
            extension=extension,
            config=config, attrs=attrs
        )
        return mark_safe('\n'.join(tags))
    except WebpackBundleLookupError:
        return ''


numeric_test = re.compile("^\d+$")
def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""

    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif numeric_test.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID
register.filter('getattribute', getattribute)


@register.simple_tag
def get_verbose_name(object):
    if(hasattr(object, '_meta')):
        return object._meta.verbose_name
    else:
        return ''

@register.simple_tag
def get_verbose_name_plural(object):
    if(hasattr(object, '_meta')):
        return object._meta.verbose_name_plural
    else:
        return ''

@register.simple_tag
def get_form_name(object):
    return object._meta.model._meta.verbose_name
