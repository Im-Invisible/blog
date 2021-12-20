from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='Article')
    anons = models.CharField('Anons', max_length=200)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


