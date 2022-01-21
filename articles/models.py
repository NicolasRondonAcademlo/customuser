from django.db import models
from core.models import CustomUser

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return self.title