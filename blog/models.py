from django.db import models
from ckeditor.fields import RichTextField
from personal_django.models import BaseModel
from django.conf import settings


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
    image = models.ImageField(
        verbose_name="Image",
        help_text="Post Image",
        upload_to="posts"
    )

    @property
    def image_absolute_path(self):
        return f"{settings.SITE_DOMAIN}media/{self.image}"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-create_date",)
