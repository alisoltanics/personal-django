# Generated by Django 3.0.5 on 2020-04-25 07:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='Create Date', verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, help_text='Update Date', verbose_name='Update Date')),
                ('title', models.CharField(help_text='Post Title', max_length=400, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(help_text='Post Description', verbose_name='Description')),
                ('published', models.BooleanField(default=False, help_text='Post Published', verbose_name='Published')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
