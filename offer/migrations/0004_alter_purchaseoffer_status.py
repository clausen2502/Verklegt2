# Generated by Django 5.2 on 2025-05-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_purchaseoffer_contingent_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseoffer',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('contingent', 'Contingent'), ('finalized', 'Finalized')], default='pending', max_length=10),
        ),
    ]
