# Generated by Django 4.2.2 on 2023-06-27 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_autor_livro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]