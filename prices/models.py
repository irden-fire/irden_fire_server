from django.db import models

#here you can find name and duration used by default
class Price(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    duration = models.CharField(max_length=100, blank=True, default='')
    how_many_participants = models.IntegerField(blank=True)
    description = models.TextField()

    class Meta:
        ordering = ('cost',)

    def __str__(self):
        return self.name + ' ' + str(self.cost)

#Here you can find additional name and duration for custom locales
class PriceDescription(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    language = models.CharField(max_length=4, blank=True, default='ru')
    price = models.ForeignKey(Price, blank=True, null=True, related_name='description_l18n')

    def __str__(self):
        return self.language
