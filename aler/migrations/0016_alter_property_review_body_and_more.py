# Generated by Django 4.0.4 on 2022-11-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aler', '0015_alter_property_review_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_review',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='property_review',
            name='creator',
            field=models.CharField(max_length=500, null=True),
        ),
    ]