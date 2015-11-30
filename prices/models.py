from django.db import models

class Price(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    duration = models.CharField(max_length=100, blank=True, default='')
    how_many_participants = models.IntegerField(blank=True)
    description = models.TextField()

    class Meta:
        ordering = ('cost',)

    def __str__(self):              # __unicode__ on Python 2
        return self.name + ' ' + str(self.cost)
