from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(widget= forms.Textarea,label="Description", max_length=200)