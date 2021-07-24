

from umb.admin.models import Master, Weight
from django import forms

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = '__all__'

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'