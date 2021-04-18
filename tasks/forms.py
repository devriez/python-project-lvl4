from django.forms import ModelForm

from tasks.models import Task


class RegisterTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = "Имя"
        self.fields['description'].label = "Описание"
        self.fields['status'].label = "Статус"
        self.fields['executor'].label = "Исполнитель"
        self.fields['labels'].label = "Метки"

        