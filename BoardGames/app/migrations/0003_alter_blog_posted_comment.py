# Generated by Django 4.2.7 on 2023-12-07 19:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_blog_autor_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 7, 22, 47, 12, 214011), verbose_name='Опубликованно'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 7, 22, 47, 12, 215026), verbose_name='Дата комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blog', verbose_name='Статья комментария')),
            ],
            options={
                'verbose_name': 'Комментарии к статье блога',
                'verbose_name_plural': 'Комментарии к статьям блога',
                'db_table': 'Comment',
                'ordering': ['-date'],
            },
        ),
    ]
