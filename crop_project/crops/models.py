from django.db import models


# This model represents the crop data stored in the database
# Each row contains information about one crop record
class CropData(models.Model):

    # Stores the year the crop data belongs to
    year = models.IntegerField()

    # Stores the region where the crop was recorded
    region = models.CharField(max_length=100)

    # Stores the name of the crop (example: Wheat, Corn)
    crop = models.CharField(max_length=100)

    # Stores the total production amount
    # null=True allows empty values in the database
    # blank=True allows empty values in forms
    production = models.FloatField(null=True, blank=True)

    # Stores the crop yield amount
    yield_amount = models.FloatField(null=True, blank=True)

    # This controls how the object appears in Django admin
    # It makes records easier to read instead of showing object IDs
    def __str__(self):
        return f"{self.crop} ({self.region}, {self.year})"