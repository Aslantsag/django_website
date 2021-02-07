from django import forms
from .models import Blog
from .models import Comments

class FeedBack(forms.Form):
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {
            'class': 'about-feedback__intext left',
            'placeholder': 'Имя *'
        }
    ))
    user_phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {
            'class': 'about-feedback__intext right',
            'placeholder': 'Номер телефона *'
        }
    ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs = {
            'class': 'about-feedback__textarea',
            'placeholder': 'Расскажите о задачах которые нам надо будет решить'
        }
    ))

class ContanctForm(forms.Form):
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {
            'class': 'about-feedback__intext',
            'placeholder': 'Имя *'
        }
    ))
    user_phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {
            'class': 'about-feedback__intext',
            'placeholder': 'Номер телефона *'
        }
    ))
    user_email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs = {
            'class': 'about-feedback__intext',
            'placeholder': 'E-mail *'
        }
    ))

class Sendpost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'slug', 'text']
        widgets = {
            'image': forms.FileInput(
            attrs = {
                'class': 'blog-post__intext',
            }),
            'title': forms.TextInput(
            attrs={
                'id': 'post-title',
                'class': 'blog-post__intext',
                'placeholder': 'Заголовок',
                'autocomplete': 'off'
            }),
            'slug': forms.TextInput(
            attrs={
                'id': 'post-slug',
                'class': 'blog-post__intext',
                'placeholder': 'ЧПУ',
                'autocomplete': 'off'
            }),
            'text': forms.Textarea(
            attrs={
                'class': 'blog-post__intext',
                'placeholder': 'Заголовок'
            }),
        }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(
            attrs={
                'id': 'post-title',
                'class': 'blog-commnets__intext',
                'placeholder': 'Ваше имя',
                'autocomplete': 'off'
            }),
            'text': forms.Textarea(
            attrs={
                'class': 'blog-commnets__textarea',
                'placeholder': 'Введите ваш комментарий'
            }),
        }
