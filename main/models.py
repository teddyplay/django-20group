from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=50)
    rate = models.PositiveIntegerField(default=0, max_length=10, verbose_name="Рейтинг")
    duration = models.DurationField(verbose_name="Продолжительность")
    image = models.ImageField(upload_to="" , null=True)


    def __str__(self):
        return self.title

class Rewiev(models.Model):
    id_pole = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete = models.CASCADE)
    text = models.TextField(max_length=500, verbose_name="Текст")

    def __str__(self):
        return self.id_pole

    # producer = models.CharField(max_length=100, verbose_name="Продюссер")
    # rate = models.CharField(choices=choices, max_length=255, default=0.0)
    # duration = models.DurationField(verbose_name="продолжительность")
