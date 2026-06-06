from django.forms import ModelForm, widgets
from django.core.validators import EmailValidator
from records.models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'email', 'text']
        widgets = {
            "text": widgets.Textarea(attrs={"cols": "40", "rows": "5"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        validator = EmailValidator(message="Неверный email")
        validator(email)
        return email