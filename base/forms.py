from django import forms

from base.models import Employer


class EmployerForm(forms.ModelForm):

        class Meta:
            model = Employer
            fields = ['name', 'link', 'address', 'vacancy_count','sector',]
