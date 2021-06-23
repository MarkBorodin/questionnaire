# Generated by Django 3.1 on 2021-03-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_generator', '0013_auto_20210308_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('write_date', models.DateTimeField(auto_now=True, null=True)),
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('client_address', models.TextField(max_length=512, null=True)),
                ('client_name', models.TextField(max_length=128, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('description', models.TextField(max_length=512, null=True)),
                ('iban', models.TextField(default='CH26 0483 5216 7077 3100 0', max_length=32, null=True)),
                ('bic_swift', models.TextField(default='CRESCHZZ80A', max_length=32, null=True)),
                ('kontonummer', models.TextField(default='2167077-32', max_length=32, null=True)),
                ('bemerkung', models.TextField(blank=True, max_length=512, null=True)),
                ('zahlbar_bis', models.DateTimeField(null=True)),
                ('netto_price', models.IntegerField(null=True)),
                ('mwst', models.IntegerField(null=True)),
                ('invoice_amount_total', models.IntegerField(null=True)),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='pdf_generator.offer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
