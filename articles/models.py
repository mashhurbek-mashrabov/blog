from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200, null=True, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def created_at(self):
        return f"{self.date.strftime('%X')} {self.date.strftime('%x')}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True)
    comment = models.CharField(max_length=150, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    @property
    def created_at(self):
        return f"{self.date.strftime('%X')} {self.date.strftime('%x')}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.article.pk)])
