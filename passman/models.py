import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, db_index=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True, blank=False, null=False)
    url = models.URLField(blank=True, db_index=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = 'sites'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Password(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    username = models.CharField(max_length=255, db_index=True, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, db_index=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'password'
        verbose_name_plural = 'passwords'
        ordering = ('username', 'url')

    def __str__(self):
        return self.username
