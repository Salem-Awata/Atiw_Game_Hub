from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cover_image_url = models.URLField(blank=True, null=True)
    template_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='scores')
    player_initials = models.CharField(max_length=3)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return f"{self.player_initials} - {self.score} on {self.game.title}"
