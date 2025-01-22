from django.db import models

# Create your models here.
class ReadEntry(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    CATEGORY_CHOICES = (
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('fantasy', 'Fantasy'),
        ('biography', 'Biography'),
    )
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    STATUS_CHOICES = (
        ('incomplted','incompleted'),
        ('inprogress','inprogress'),
        ('complted','completed'),
    )
    status = models.CharField(max_length=30,choices=STATUS_CHOICES)

    total_pages = models.PositiveIntegerField()
    pages_read = models.PositiveIntegerField(default=0)
    progress = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=False)

    def save(self, *args, **kwargs):
        if self.total_pages > 0:
            self.progress = int((self.pages_read / self.total_pages) * 100)
        else:
            self.progress = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title