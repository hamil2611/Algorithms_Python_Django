# Generated by Django 4.0.2 on 2022-06-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_document_id_document_doc_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='dictionary',
            field=models.CharField(default=None, max_length=100),
        ),
    ]