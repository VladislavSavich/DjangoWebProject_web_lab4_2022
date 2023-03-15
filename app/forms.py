"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Comment
from .models import Blog
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Оцените сайт от 1 до 5',
                             choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')],
                             widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Какова вероятность что вы посоветуете наш сайт другому человеку?',
                                 choices=(('1','Не посоветую'),
                                          ('2','Возможно посоветую'),
                                          ('3','Посоветую'),
                                          ('4','Обязательно посоветую')), initial=1)
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                               required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Что бы вы хотели изменить на сайте?',
                              widget=forms.Textarea(attrs={'rows':12,'cols':20})) 

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Описание", 'content': "Полное содержание", 'image': "Картинка"}
