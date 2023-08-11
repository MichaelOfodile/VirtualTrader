from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class StockData(models.Model):
    symbol = models.TextField(null=True)
    data = models.TextField(null=True)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')

        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, password, **extra_fields)
    
   
# why cant people log in after just creating an account?

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
