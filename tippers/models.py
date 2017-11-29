from django.db import models

class TipperModels(models.Model):

    title = models.CharField(max_length=100)
    carrying = models.FloatField()

    def __str__(self):
        return self.title


class TipperMachines(models.Model):

    model = models.ForeignKey(TipperModels)
    number = models.CharField(max_length=30)

    def __str__(self):
        return self.number

class CurrentTrip(models.Model):
    machine = models.ForeignKey(TipperMachines)
    weight = models.FloatField()

    @property
    def machine_number(self):
        return self.machine.number

    @property
    def machine_title(self):
        return self.machine.model.title

    @property
    def machine_carrying(self):
        return self.machine.model.carrying


    @property
    def machine_overload(self):
        return max(round((self.weight - self.machine_carrying) / self.machine_carrying *100, 2), 0)
