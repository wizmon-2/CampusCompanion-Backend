from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class AccountManager(BaseUserManager):
    def create_user(self, userid, password, **extra_fields):
        if not userid:
            raise ValueError(_("The userid must be set"))
        user = self.model(userid=userid,groups=userid, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, userid, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(userid, password, **extra_fields)
