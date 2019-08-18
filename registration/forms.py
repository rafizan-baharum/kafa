from django import forms

from .models import Applicant

class ApplicantForm(forms.Form):
    mykid_no = forms.CharField()
    name = forms.CharField()
    address1 = forms.CharField()
    address2 = forms.CharField()
    address3 = forms.CharField()
    remarks = forms.CharField(widget=forms.Textarea)
    registered_date = forms.DateField()


class ApplicantModelForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['mykid_no', 'name', 'address1', 'address2', 'address3', 'registered_date']

    def clean_mykid_no(self, *args, **kwargs):
        instance = self.instance
        mykid_no = self.cleaned_data.get('mykid_no')
        qs = Applicant.objects.filter(mykid_no__iexact=mykid_no)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This mykid no has already been registered. Please try again.")
        return mykid_no
