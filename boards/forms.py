from django import forms

from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': '여기에 당신의 생각을 써주세요.'}
        ),
        max_length=4000,
        help_text='4000 글자까지 입력할수 있습니다.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    message = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': '여기에 당신의 생각을 써주세요.'}
        ),
    )

    class Meta:
        model = Post
        fields = ['message', ]
