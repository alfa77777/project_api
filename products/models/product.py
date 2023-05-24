import random

from django.db import models
from django.utils.text import slugify

from common.models import TimestampModel


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="products", null=True)
    category = models.ForeignKey("common.Category", on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey("common.Brand", on_delete=models.CASCADE, related_name="products", null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        slug = self.slug
        while self.__class__.objects.filter(slug=slug).exists():
            slug = f"{self.slug}-{random.randint(1, 100000)}"
        self.slug = slug
        return super().save(*args, **kwargs)

    @property
    def likes(self):
        return self.like_dislikes.filter(type=LikeDislike.LikeType.LIKE).count()

    @property
    def dislikes(self):
        return self.like_dislikes.filter(type=LikeDislike.LikeType.DISLIKE).count()


class LikeDislike(TimestampModel):
    class LikeType(models.IntegerChoices):
        DISLIKE = -1
        LIKE = 1

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="like_dislikes")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="like_dislikes")
    type = models.SmallIntegerField(choices=LikeType.choices)

    class Meta:
        unique_together = ["product", "user"]

    def __str__(self):
        return f"{self.user}"
