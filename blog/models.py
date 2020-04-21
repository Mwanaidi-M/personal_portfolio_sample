from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    blog_date = models.DateField()
    blog_text = models.TextField()

    def __str__(self):
        return self.title
