# Generated by Django 5.0.4 on 2024-07-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_sc2_record_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sc2',
            name='id2',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='sc2',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
