# Generated by Django 4.2.7 on 2023-11-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_credito', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]