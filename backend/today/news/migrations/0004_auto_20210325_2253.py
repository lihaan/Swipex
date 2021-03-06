# Generated by Django 3.1.4 on 2021-03-25 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('reader_no', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=255)),
                ('has_read', models.ForeignKey(db_column='news_id', on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
