# Generated by Django 4.2.7 on 2023-12-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0006_tarefas_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='email',
            field=models.TextField(max_length=255),
        ),
    ]