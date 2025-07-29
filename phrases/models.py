from django.db import models

# Create your models here.

class MotivationalPhrase(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('study', 'Study'),
        ('love', 'Love'),
        ('sports', 'Sports'),
        ('life', 'Life'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category}: {self.text[:50]}..."
