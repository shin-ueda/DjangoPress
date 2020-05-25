from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey('Category', verbose_name='Category',
                                 on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey('Tag', verbose_name='Tag', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = now
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')

    class Meta:
        verbose_name = 'Tag'
        ordering = ['title']

    def __str__(self):
        return self.title
