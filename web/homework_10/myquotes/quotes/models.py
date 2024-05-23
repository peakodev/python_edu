import ast

from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=256)
    born_date = models.DateTimeField()
    born_location = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'fullname'], name='authors of username')
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    _tags = models.TextField(db_column='tags')
    pab_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'quote'], name='quotes of username')
        ]

    @property
    def tags(self):
        return ast.literal_eval(self._tags if self._tags else '[]')

    @tags.setter
    def tags(self, value):
        print("Valuye = {value}")
        self._tags = str(value)

    def __str__(self):
        return f"{self.quote}"
