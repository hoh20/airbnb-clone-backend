from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """Room model definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_PLACE = ("private_place", "Private Place")
        SHARED_PLACE = ("shared_place", "Shared Place")

    name = models.CharField(max_length=150, default="",)
    country = models.CharField(max_length=50, default="Canada",)
    city = models.CharField(max_length=50, default="Toronto",)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=False,)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        return self.amenities.count()


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(max_length=150,)
    description = models.CharField(max_length=150, null=True, blank=True,)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"