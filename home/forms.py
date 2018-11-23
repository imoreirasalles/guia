from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(
        label=_('Username or Email'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            filters = {}
            if '@' in username:
                filters['email'] = username
            else:
                filters['username'] = username

            user = User.objects.get(**filters)
            if not user.email:
                raise forms.ValidationError(
                    _('User "{username}" doesn\'t have e-mail').format(username=username)
                )

            return user
        except User.DoesNotExist:
            raise forms.ValidationError(
                _('User "{username}" not found').format(username=username)
            )


class ResetPasswordForm(forms.ModelForm):
    new_password = forms.CharField(
        label=_('New pasword'),
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label=_('Confirm pasword'),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['new_password', 'confirm_password']

    def clean(self):
        data = self.cleaned_data
        if data['new_password'] != data['confirm_password']:
            self.add_error('new_password', _('The passwords are not equals'))
            self.add_error('confirm_password', _('The passwords are not equals'))

        return data
