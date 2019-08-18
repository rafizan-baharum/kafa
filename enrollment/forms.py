from django import forms

from .models import Session

class SessionForm(forms.Form):
    code = forms.CharField()
    name = forms.CharField()
    opened = forms.BooleanField()

class SessionModelForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['code', 'name', 'opened']

    def clean_code(self, *args, **kwargs):
        instance = self.instance
        code = self.cleaned_data.get('code')
        qs = Session.objects.filter(code__iexact=code)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This code has already been registered. Please try again.")
        return code