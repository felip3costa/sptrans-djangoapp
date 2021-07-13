# Generated by Django 3.2.5 on 2021-07-12 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0006_paradaporlinha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradaporlinha',
            name='linha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transporte.linha', unique=True),
        ),
        migrations.AlterField(
            model_name='paradaporlinha',
            name='parada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transporte.parada', unique=True),
        ),
    ]