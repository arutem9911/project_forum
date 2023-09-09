from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model


class Topic(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=3000,
        null=False,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at'
    )

    author = models.ForeignKey(
        'accounts.user',
        on_delete=models.CASCADE,
        default=1,
        related_name='topics',
        verbose_name='author'
    )

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    def __str__(self):
        return f'{self.title}'
