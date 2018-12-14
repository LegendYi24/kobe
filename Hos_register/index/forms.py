from django import forms

class Pat_Login_Form(forms.Form):
    name = forms.CharField(
        label='姓名',
        widget=forms.TextInput(
            attrs={'placeholder': '请输入姓名'}
        )
    )
    phone = forms.CharField(
        label='手机号码',
        widget=forms.TextInput(
            attrs={'placeholder': '输入手机号码以便通知'}
        )
    )
    id = forms.CharField(
        label='身份证号',
        widget=forms.TextInput(
            attrs={'placeholder': '请输入身份证号码'}
        )
    )


class Doc_Login_Form(forms.Form):
    account = forms.CharField(
        label='登录账号',
        widget=forms.TextInput(
            attrs={'placeholder': '请输入帐号'}
        )
    )
    pwd = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(
            attrs={'placeholder': '请输入密码'}
        )
    )