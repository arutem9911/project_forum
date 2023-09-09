from django.db import models
# from django.contrib.auth import get_user_model


class Comment(models.Model):
    comment_text = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='comment_text'
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='created at'
    )

    topic = models.ForeignKey(
        'forum.Topic',
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name='comment',
        verbose_name='topic')

    author = models.ForeignKey(
        'accounts.user',
        on_delete=models.CASCADE,
        default=1,
        related_name='comments',
        verbose_name='author'
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.comment_text} | {self.created_at} | {self.topic}'
