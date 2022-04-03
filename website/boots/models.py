from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return f'ID {self.id}: name: {self.name}'

    def get_absolute_url(self):
        return reverse('acticle_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Товары'

