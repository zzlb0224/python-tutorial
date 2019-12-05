from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2,
                            label="标题", error_messages={'min_length': '最少需要两个字符'})
    content = forms.CharField(widget=forms.Textarea, label="内容")
    email = forms.EmailField(label="邮箱")
    reply = forms.BooleanField(required=False, label="是否回复")
