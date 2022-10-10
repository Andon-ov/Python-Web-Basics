# Generated by Django 4.1.2 on 2022-10-10 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('food_type', models.CharField(choices=[('Soup', 'Soup'), ('Salad', 'Salad'), ('Appetizer', 'Appetizer'), ('Pasta', 'Pasta'), ('Main Dish', 'Main Dish'), ('Pizza', 'Pizza'), ('Dessert', 'Dessert'), ('Base', 'Base')], max_length=9)),
                ('image_url', models.URLField()),
                ('instructions', models.TextField()),
                ('ingredient', models.ManyToManyField(related_name='+', to='recipes.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='base',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='base', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recipes.measure'),
        ),
    ]