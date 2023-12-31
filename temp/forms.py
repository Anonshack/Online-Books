from django import forms
from .models import Books, QrCode


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['image', 'file', 'title']


class QR_code_mainly(forms.ModelForm):
    class Meta:
        model = QrCode
        fields = ['title', 'image', 'info', 'url']
