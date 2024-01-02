from django.db import models

class NewsArticle(models.Model):
    end_year = models.CharField(max_length=50, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=200)
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=50, blank=True)
    impact = models.CharField(max_length=100, blank=True)
    added = models.CharField(max_length=50)
    published = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.TextField()
    likelihood = models.IntegerField()

    def __str__(self):
        return self.title
