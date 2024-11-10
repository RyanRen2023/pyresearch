from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=200)
    log_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on ({date:%Y-%m-%d %H:%M})"

