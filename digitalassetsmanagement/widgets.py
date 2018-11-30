import re
from django import forms
from django.conf import settings


class MultipleSelectPreviewImageWidget(forms.CheckboxSelectMultiple):
    option_template_name = 'forms/widgets/preview_image_checkbox_option.html'
    REGEX = '\[([\w+]+)\][\w ]+\[([\w_\-.]+)\]'

    @property
    def media(self):
        return forms.Media(js=['js/widget-preview-image.js'])

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=None, attrs=None)
        option['attrs']['data-capture-url'] = ''

        rm = re.search(self.REGEX, option['label'])
        if rm:
            option['capture_url'] = '{}{}'.format(settings.MEDIA_URL, rm.group(2))
        return option

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['class'] = 'capture-preview-image'
        return context
