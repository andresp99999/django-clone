# Generated by Django 2.2.7 on 2019-11-04 13:46

from django.db import migrations, models
import model_clone.mixins.clone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            bases=(model_clone.mixins.clone.CloneMixin, models.Model),
        ),
    ]
