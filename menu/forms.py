from django import forms


from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
