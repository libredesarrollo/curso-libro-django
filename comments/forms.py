from django.forms import ModelForm, Textarea

from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text' : Textarea(attrs={'class':'form-input'})
        }
    """def save(self,commit=True, text=""):
        instance = super(CommentForm, self).save(commit=commit)

        if(text != ""):
            instance.text= text#"No podrás modificarme"

        if(commit):
            instance.save()
        
        return instance"""
