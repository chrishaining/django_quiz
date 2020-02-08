# Generated by Django 3.0 on 2020-02-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20200207_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=6)),
                ('url', models.URLField(max_length=250)),
            ],
        ),
    ]
