from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 通过用户名或邮箱来获取用户对象
            user = User.objects.get(
                Q(username=username) |
                Q(mobile = username)
            )
            # 验证用户的密码
            if user.check_password(password):
                return user
        except Exception:
            return None