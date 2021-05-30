from django import forms
from covetgroup import models


class SubscribeToPDF(forms.ModelForm):
    class Meta:
        model = models.SubscribedUser
        fields = "__all__"
