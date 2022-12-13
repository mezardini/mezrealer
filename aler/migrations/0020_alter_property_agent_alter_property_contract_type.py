# Generated by Django 4.0.4 on 2022-11-21 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aler', '0019_alter_property_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aler.agent'),
        ),
        migrations.AlterField(
            model_name='property',
            name='contract_type',
            field=models.CharField(choices=[('rent', 'Rent'), ('sale', 'Sale')], max_length=50),
        ),
    ]
