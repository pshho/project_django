from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    choices = [
        ()
    ]

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'file', 'category']
        labels = {
            'title':'제목',
            'content':'내용',
            'photo':'사진',
            'file':'파일',
            'category':'분류',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control my-2'
