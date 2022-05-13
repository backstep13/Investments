from django.db import models


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
