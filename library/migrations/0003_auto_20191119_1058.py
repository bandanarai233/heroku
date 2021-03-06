# Generated by Django 2.1 on 2019-11-19 05:13

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_book_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Class',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Contact',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AddField(
            model_name='student',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
