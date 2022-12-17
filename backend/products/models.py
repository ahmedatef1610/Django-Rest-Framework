from django.db import models
from django.db.models import Q
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL

import random
#################################################################
TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']

class ProductQuerySet(models.QuerySet):
    
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        # return self.filter(title__icontains=query)
    
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            # qs = qs.filter(user=user)
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        # return Product.objects.filter(public=True).filter(title__icontains=query)
        # return self.get_queryset().is_public().filter(title__icontains=query)
        # return self.get_queryset().is_public().search(query, user=user)
        return self.get_queryset().search(query, user=user)
    

class Product(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=1)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    public = models.BooleanField(default=True)
    
    objects = ProductManager()
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.id} - {self.title}"



    def is_public(self):
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    
    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.pk}/"
    
    @property
    def body(self):
        return self.content
    
    @property
    def sale_price(self):
        # return "%.2f" %(float(self.price) * 0.8)
        return f"{float(self.price) * 0.8:.2f}"

    def get_discount(self):
        return "122"
