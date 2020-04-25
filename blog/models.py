from django.db import models
from ckeditor.fields import RichTextField
from personal_django.models import BaseModel


class Post(BaseModel):
    """Data model for Post"""

    title = models.CharField(
        verbose_name="Title",
        max_length=400,
        help_text="Post Title"
    )
    description = RichTextField(
        verbose_name="Description",
        help_text="Post Description"
    )
    published = models.BooleanField(
        default=False,
        verbose_name="Published",
        help_text="Post Published",
    )
