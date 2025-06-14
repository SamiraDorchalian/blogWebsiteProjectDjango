from django.shortcuts import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', _('Published')),
        ('drf', _('Draft')),
    )

    title = models.CharField(max_length=100, verbose_name=_('Title'))
    text = models.TextField(verbose_name=_('Comment Text'))
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('author'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, verbose_name=_('Status'))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
    
