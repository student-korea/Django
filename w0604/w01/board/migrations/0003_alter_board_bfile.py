# Generated by Django 5.2.1 on 2025-06-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_bfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bfile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
