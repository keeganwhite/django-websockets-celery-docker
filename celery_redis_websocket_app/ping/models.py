from django.db import models
from django.core.validators import RegexValidator

# validator to ensure the MAC address format is correct
mac_address_validator = RegexValidator(
    regex=r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$',
    message="Enter a valid MAC address in format XX:XX:XX:XX:XX:XX."
)

class Host(models.Model):
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    ip_address = models.GenericIPAddressField(
        unique=True,
    )
    mac_address = models.CharField(
        max_length=17,
        blank=True,
        null=True,
        unique=True,
        validators=[mac_address_validator],
    )

    def __str__(self):
        return self.name if self.name else self.ip_address

class PingResult(models.Model):
    host = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        related_name='ping_results'
    )
    is_alive = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Alive" if self.is_alive else "Down"
        return f"{self.host} at {self.timestamp}: {status}"
