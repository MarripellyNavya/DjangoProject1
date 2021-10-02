from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Product(models.Model):
    CATG_CHOICES = (
        ('mobileph', 'Mobile Phone'),
    )
    name = models.CharField(max_length=20)
    catg = models.CharField(max_length=10,
                            choices=CATG_CHOICES,
                            default='mobileph')
    slug = models.SlugField(max_length=30, unique_for_date='publish')
    desc = models.TextField()
    pic = models.ImageField(upload_to='product_pic', blank=True, null=True, )
    dataEntryBy = models.ForeignKey(User,
                                    related_name='product_user',
                                    on_delete=models.CASCADE, )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail',
                       args=[self.slug]
                       )
    def get_absolute_url(self):
        return reverse('mobile:Product_detail',
                       args=[
                           self.slug]
                       )
