from django.db import models
from django.urls import reverse

# Create your models here.

class topMenu(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('top_menu', kwargs={'item_menu_id': self.pk})


class topSubMenu(models.Model):
    top = models.ForeignKey(topMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sub_menu', kwargs={'sub_item_menu_id': self.pk})
