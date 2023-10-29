# Generated by Django 4.2.6 on 2023-10-28 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_active_category_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, upload_to='', verbose_name='Lesson/ %Y %m')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='active',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='category',
            name='update_date',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Course/ %Y %m'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.tag')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_%(class)s_related', to='courses.tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('courses.tag',),
        ),
    ]
