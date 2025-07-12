from django.db import models

class StudentRecord(models.Model):
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.reg_number})"
