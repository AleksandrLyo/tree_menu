from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Menu name'
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name="Menu slug"
    )

    class Meta:
        verbose_name = 'Menu'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Item name'
    )
    slug = models.SlugField(
        max_length=64,
        verbose_name="Item slug"
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        null=True,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name="Menu"
    )
    parent = models.ForeignKey(
        'Item',
        blank=True,
        null=True,
        related_name='childrens',
        on_delete=models.CASCADE,
        verbose_name="Parent"
    )

    class Meta:
        verbose_name = 'Menu item'

    def __str__(self):
        return self.name