from django import template
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.simple_tag(takes_context=True)
def th_with_order_by(context, field, label, *args, **kwargs):
    request = context['request']

    label = _(label)
    icon = ''

    if field in request.GET.get('order_by', ''):
        icon = '<i class="fa fa-long-arrow-up"></i>'
        if '-' in request.GET.get('order_by'):
            icon = '<i class="fa fa-long-arrow-down"></i>'

    return format_html('<a href="javascript:order_by(\'{field}\')">{label} {icon}</a>'.format(
        field=field, label=label, icon=icon))


@register.filter
def boolean_with_icons(value, *args, **kwargs):
    if value is None:
        return format_html('<i class="fal fa-question-circle"></i>')
    elif not value:
        return format_html('<i class="fas fa-times-circle bullet-times"></i>')
    else:
        return format_html('<i class="fas fa-check-circle bullet-check"></i>')


@register.simple_tag(takes_context=True)
def checkbox_with_switch(context, field_name, *args, **kwargs):
    request = context['request']

    checked = ''
    state = 'false'
    if request.GET.get(field_name) and request.GET.get(field_name) == 'on':
        checked = 'checked'
        state = 'true'

    return format_html('<input type="checkbox" name="{field_name}" id="id_{field_name}" ' \
           'class="bootstrap-switch" {checked} data-state="{state}" data-on-text="SIM" ' \
           'data-off-text="NÃO">'.format(field_name=field_name, checked=checked, state=state))