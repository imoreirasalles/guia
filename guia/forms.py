from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            if not user.email:
                raise forms.ValidationError(
                    _('User "{username}" doesn\'t have e-mail').format(username=username)
                )

            return user
        except User.DoesNotExist:
            raise forms.ValidationError(
                _('User "{username}" not found').format(username=username)
            )
