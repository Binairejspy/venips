# Generated by Django 4.0 on 2022-01-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0007_alter_concepts_freelance_nomfreelance'),
    ]

    operations = [
        migrations.AddField(
            model_name='concepts_freelance',
            name='designation',
            field=models.CharField(default='concepte', max_length=50),
        ),
    ]
