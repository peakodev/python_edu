from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, Textarea
from .models import Author, Quote


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=256, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput(attrs={'type': 'date'}))
    born_location = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    description = CharField(min_length=3, required=True, widget=Textarea())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    quote = CharField(min_length=3, required=True, widget=TextInput())
    tags = CharField(min_length=3, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'tags']
        exclude = ['author']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        return [tag.strip() for tag in tags.split(',')]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.tags = self.cleaned_data.get('tags')
        if commit:
            instance.save()
        return instance
