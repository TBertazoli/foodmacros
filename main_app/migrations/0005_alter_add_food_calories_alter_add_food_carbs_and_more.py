# Generated by Django 5.0.4 on 2024-05-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_alter_add_food_options_add_food_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="add_food",
            name="calories",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="add_food",
            name="carbs",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="add_food",
            name="fat",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="add_food",
            name="protein",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="add_food",
            name="weight",
            field=models.FloatField(blank=True, null=True),
        ),
    ]