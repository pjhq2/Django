from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        min_length=2,  # models.py에서 할 수 없는 걸 forms.py에서 오버라이딩을 통해 작성할 수 있다.
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요',
                'maxlength': 30,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요',
            }
        )
    )
    # 이게 있으면 blank=True가 안먹히는 이유가 뭘까..
    # image = forms.ImageField(
    #     label='이미지',
    # )
    class Meta:
        model = Article
        fields = '__all__'
