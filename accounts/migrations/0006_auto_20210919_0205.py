# Generated by Django 3.2.7 on 2021-09-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210919_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='costumer',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
