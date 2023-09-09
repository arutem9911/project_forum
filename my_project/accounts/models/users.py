from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='profile'
    )

    birth_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='birth date'
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='avatar'
    )

    def __str__(self):
        return self.user.username + "'s Profile"

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

