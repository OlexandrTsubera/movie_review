from django.forms import Textarea, ModelForm
from .models import Reviews


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Reviews
        fields = ['text', 'watchAgain']
        labels = {'watchAgain': 'Watch Again'}
        widgets = {'text': Textarea(attrs={'rows': 4})}

