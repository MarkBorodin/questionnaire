# Generated by Django 3.1 on 2021-07-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0020_auto_20210714_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bgimage',
            name='image',
            field=models.ImageField(default='bg1.jpg', upload_to=''),
        ),
    ]
