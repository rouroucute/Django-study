import re
from django import forms
from users.models import UsersProfile

class UserRegisterForm(forms.Form):

    username = forms.CharField(
      required=True,
      widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    mobile = forms.CharField(
      min_length=11,
      max_length=11,
      required=True,
      widget=forms.NumberInput(attrs={'class':'form-control'}),
    )



    # 针对指定字段添加自定义验证
    # 方法名格式要求:  clean_字段名
    def clean_mobile(self):
        """
        验证手机号是否合法
        :return: 合法的数据或者错误信息
        """
        mobile = self.cleaned_data['mobile']
        PRGEX_MOBILE = r'^1[358]\d{9}|^147\d{8}|^176\d{8}$'
        regex = re.compile(PRGEX_MOBILE)
        if regex.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(
                '无效的手机号',
                code='mobile_invalid'
            )


class UserRegisterModelForm(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ["username","password", "mobile",
                 ]
     
    def clean_mobile(self):
        """
        验证手机号是否合法
        :return: 合法的数据或者错误信息
        """
        mobile = self.cleaned_data['mobile']
        PRGEX_MOBILE = r'^1[358]\d{9}|^147\d{8}|^176\d{8}$'
        regex = re.compile(PRGEX_MOBILE)
        if regex.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(
                '无效的手机号',
                code='mobile_invalid'
            )

