from django.forms import ModelForm

from labels.models import Label


class RegisterLabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = "Имя"

        