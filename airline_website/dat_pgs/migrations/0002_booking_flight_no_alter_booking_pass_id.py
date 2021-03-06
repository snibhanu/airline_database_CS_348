# Generated by Django 4.0.3 on 2022-04-29 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dat_pgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='flight_no',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dat_pgs.flightlist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='pass_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dat_pgs.passlist'),
        ),
    ]
