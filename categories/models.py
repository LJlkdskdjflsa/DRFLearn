from django.db import models
from helpers.models import TrackingModel
from authentication.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel, TrackingModel):
    """
    Category Table implimented with MPTT.
    """
    title = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    description = models.TextField()
    #slug = models.SlugField(max_length=255, null=True, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

'''    def get_absolute_url(self):
        return reverse("template:category_list", args=[self.slug])

    def __str__(self):
        return self.title'''