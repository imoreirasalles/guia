from django import template
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.simple_tag(takes_context=True)
def th_with_order_by(context, field, label, *args, **kwargs):
    request = context['request']

    label = _(label)
    icon = ''

    if field in request.GET.get('order_by'):
        icon = '<i class="fa fa-long-arrow-up"></i>'
        if '-' in request.GET.get('order_by'):
            icon = '<i class="fa fa-long-arrow-down"></i>'

    return format_html('<a href="javascript:order_by(\'{field}\')">{label} {icon}</a>'.format(
        field=field, label=label, icon=icon))
