from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField(choices=[
        (5, 'Excelente'),
        (4, 'Bom'),
        (3, 'Regular'),
        (2, 'Ruim'),
        (1, 'Péssimo'),
    ])

    def __str__(self):
        return f"{self.name} - {self.get_rating_display()}"
