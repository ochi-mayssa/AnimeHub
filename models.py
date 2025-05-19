from django.db import models
from core.models import Genre

class Manga(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='manga_covers/')
    genres = models.ManyToManyField(Genre, related_name='manga')
    author = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('ongoing', 'En cours'),
        ('completed', 'Terminé'),
        ('hiatus', 'En pause'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    rating = models.FloatField(default=0.0)
    @property
    def latest_chapter(self):
        last_chapter = self.chapter_set.order_by('-chapter_number').first()
        return last_chapter.chapter_number if last_chapter else 0

    def __str__(self):
        return self.title

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    chapter_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.manga.title} - Chapitre {self.chapter_number}"

class Page(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='manga_pages/')