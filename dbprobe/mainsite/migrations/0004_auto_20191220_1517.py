# Generated by Django 2.2.7 on 2019-12-20 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='crew',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainsite.Crew'),
        ),
    ]
