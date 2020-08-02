from datetime import time

from django.db import models


# Create your models here.
class Room(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} at {self.floor} floor on room {self.room_number} "


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} (time) on {self.date} (date) "
