from django.db import models

class Classification(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class ClassificationItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.ManyToManyField(Classification)

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return self.item_name
