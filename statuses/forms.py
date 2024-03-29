from django.forms import ModelForm
from statuses.models import Status


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
