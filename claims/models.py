from django.db import models
from django.conf import settings
from items.models import LostItem, FoundItem

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)

class Claim(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE, null=True, blank=True)
    found_item = models.ForeignKey(FoundItem, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.lost_item:
            return f"{self.user.email} claims Lost: {self.lost_item.name}"
        elif self.found_item:
            return f"{self.user.email} claims Found: {self.found_item.name}"
        return f"{self.user.email} Claim"
