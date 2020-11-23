from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Classification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file_name = models.CharField(max_length=100, default='')
    file_description = models.CharField(max_length=255, default='')
    file_type = models.CharField(max_length=5, default='')
    document = models.FileField(upload_to='files', default='')

    class Meta:
        ordering = ['file_name']

    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return reverse('home')

class ClassificationItem(models.Model):
    item_name = models.CharField(max_length=100, default='')
    item_type = models.ForeignKey(Classification, on_delete=models.CASCADE, default='')

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return self.item_name
