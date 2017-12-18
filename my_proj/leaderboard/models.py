from django.db import models

# Create your models here.

class participant(models.Model):
    full_name = models.CharField(max_length = 50, blank = False)
    score = models.DecimalField(max_digits = 5, decimal_places = 2, help_text = 'Enter a score between 0.00 and 50.00')
    time_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    time_updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    associated_text = models.CharField(max_length = 20, default = "")

    def __str__(self):
        return str(self.full_name)
