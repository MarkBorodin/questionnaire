# Generated by Django 3.1 on 2021-04-09 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_generator', '0021_auto_20210409_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('write_date', models.DateTimeField(auto_now=True, null=True)),
                ('currency', models.TextField(default='CHF', max_length=32, null=True)),
                ('iban', models.TextField(default='CH26 0483 5216 7077 3100 0', max_length=32, null=True)),
                ('bic_swift', models.TextField(default='CRESCHZZ80A', max_length=32, null=True)),
                ('kontonummer', models.TextField(default='2167077-32', max_length=32, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='offer',
            name='bic_swift',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='iban',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='kontonummer',
        ),
        migrations.AddField(
            model_name='offer',
            name='payment_information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offers', to='pdf_generator.paymentinformation'),
        ),
    ]
