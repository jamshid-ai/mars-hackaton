# Generated by Django 4.1 on 2022-08-14 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rightAnswerId',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')], default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='api.quiz'),
        ),
    ]
