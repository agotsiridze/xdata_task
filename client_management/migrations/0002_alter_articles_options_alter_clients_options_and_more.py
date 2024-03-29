# Generated by Django 4.2.6 on 2023-10-23 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='filterwords',
            options={'verbose_name_plural': 'Filterwords'},
        ),
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='sites',
            options={'verbose_name_plural': 'Sites'},
        ),
        migrations.RemoveIndex(
            model_name='clients',
            name='clients_siteid__42aa71_idx',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='site',
            new_name='site_id',
        ),
        migrations.RenameIndex(
            model_name='articles',
            new_name='articles_site_id_67da2f_idx',
            old_name='articles_site_id_65d78b_idx',
        ),
        migrations.AlterUniqueTogether(
            name='articles',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='clients',
            name='filterwordsid',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='siteid',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='sites',
            name='internal_id',
        ),
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='filterwords',
            name='clientid',
            field=models.ForeignKey(db_column='clientid', on_delete=django.db.models.deletion.CASCADE, to='client_management.clients'),
        ),
        migrations.AlterField(
            model_name='filterwords',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sites',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='articles',
            name='article_name',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='article_text',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='found_word',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='is_top_artikle',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='screenshot_url',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='status',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='url',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='visitors_count',
        ),
    ]
