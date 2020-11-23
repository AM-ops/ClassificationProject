from django.forms import ModelForm
from .models import Classification, ClassificationItem
from django import forms

#Model Form for Annual interest rate to Nominal interest rate
class ModelFormWithFileField(ModelForm):
    class Meta:
        model = Classification
        fields = ['file_name','file_description', 'file_type', 'document']
        labels = {
        "file_name": "File Name",
        "file_description": "Description",
        "file_type": "Type (extension)",
        "document": "Choose a file",
        }
        widgets = {
        'document': forms.FileInput(attrs={'accept':'.txt, .csv, .tsv, .xls, .xlsx'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class UpdateModelForm(ModelForm):
    class Meta:
        model = ClassificationItem
        fields = ['item_name']
        labels = {
        "item_name": "Name",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)