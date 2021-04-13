from django.forms import ModelForm

from statuses.models import Status


class RegisterStatusesForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = "Имя"

        