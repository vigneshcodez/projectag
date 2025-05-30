# Generated by Django 5.1.6 on 2025-04-23 16:09

import django.core.validators
import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category')),
                ('short_description', tinymce.models.HTMLField()),
                ('description', tinymce.models.HTMLField()),
                ('faq', tinymce.models.HTMLField()),
                ('key_insights', tinymce.models.HTMLField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100, verbose_name='Business name')),
                ('business_description', models.TextField(verbose_name='Business Description')),
                ('business_address', models.TextField(default='not provided', verbose_name='Business Address')),
                ('business_since', models.DateField(blank=True, null=True, verbose_name='Business Since')),
                ('business_contact', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter a valid 10-digit mobile number.', regex='^\\d{10}$')], verbose_name='Business Mobile')),
                ('business_whatsapp', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter a valid 10-digit mobile number.', regex='^\\d{10}$')], verbose_name='Business Whatsapp')),
                ('business_image_1', models.ImageField(upload_to='business_images/', verbose_name='Profile Picture')),
                ('business_image_2', models.ImageField(blank=True, null=True, upload_to='business_images/', verbose_name='image 1')),
                ('business_image_3', models.ImageField(blank=True, null=True, upload_to='business_images/', verbose_name='image 2')),
                ('business_image_4', models.ImageField(blank=True, null=True, upload_to='business_images/', verbose_name='image 3')),
                ('business_image_5', models.ImageField(blank=True, null=True, upload_to='business_images/', verbose_name='image 4')),
                ('business_instagram_link', models.URLField(blank=True, null=True, verbose_name='Instagram link')),
                ('business_facebook_link', models.URLField(blank=True, null=True, verbose_name='Facebook Link')),
                ('business_youtube_link', models.URLField(blank=True, null=True, verbose_name='Youtube Link')),
                ('business_x_link', models.URLField(blank=True, null=True)),
                ('business_location', models.TextField(blank=True, null=True, verbose_name='Location')),
                ('business_slug', models.SlugField(blank=True, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('premium', models.BooleanField(default=False)),
                ('trusted', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('views_count', models.IntegerField(default=0)),
                ('is_top_in_category', models.BooleanField(default=False)),
                ('top_rank', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Business Category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enquired_business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.business')),
                ('enquired_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('visited_business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.business')),
                ('visited_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='location')),
                ('short_description', tinymce.models.HTMLField()),
                ('description', tinymce.models.HTMLField()),
                ('faq', tinymce.models.HTMLField()),
                ('key_insights', tinymce.models.HTMLField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.location')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='business_district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location', verbose_name='District'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(help_text='Rating must be between 1 and 5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.business')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('reviewer', 'business')},
            },
        ),
    ]
