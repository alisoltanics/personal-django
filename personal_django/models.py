from django.db import models


class BaseModel(models.Model):
    """Base model for adding extra fields to other models"""

    class Meta:
        abstract = True

    create_date = models.DateTimeField(
        verbose_name="Create Date",
        help_text="Create Date",
        auto_now_add=True,
        editable=False,
    )
    update_date = models.DateTimeField(
        verbose_name="Update Date",
        help_text="Update Date",
        auto_now=True,
        editable=False,
    )
