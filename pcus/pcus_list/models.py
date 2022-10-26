from django.db import models

# Describe model here.
class PCUS(models.Model):
    title = models.CharField(max_length=300)
    number = models.CharField(max_length=10)
    start_point = models.CharField(max_length=300, default=False)
    direction = models.CharField(max_length=300)

    def PCUS_on(self):
        print(self.title)

    def __str__(self):
        return f'{self.number}, {self.title}'


class OBJ(models.Model):
    title = models.CharField(max_length=300)
    number = models.CharField(max_length=10)
    link = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.number}, {self.title}'
