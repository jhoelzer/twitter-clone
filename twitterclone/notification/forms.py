from django import forms


class NotificationForm(forms.Form):
    viewed = forms.BooleanField(initial=False)
