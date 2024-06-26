# Generated by Django 4.2.3 on 2024-01-11 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('source', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(max_length=200)),
                ('log_type', models.CharField(max_length=50)),
                ('log_category', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('request_path', models.CharField(max_length=200)),
                ('response_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('is_public', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('reviewed_by', models.CharField(max_length=100)),
                ('reviewed_at', models.DateTimeField()),
                ('attachment', models.FileField(upload_to='attachments/')),
            ],
        ),
        migrations.CreateModel(
            name='ThreatIntelligence',
            fields=[
                ('threat_id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('last_updated', models.DateTimeField()),
                ('confidence_level', models.CharField(max_length=20)),
                ('indicator', models.CharField(max_length=100)),
                ('confidence', models.CharField(max_length=20)),
                ('source_url', models.URLField()),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='logevent',
            name='message',
            field=models.TextField(default='null'),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('incident_id', models.AutoField(primary_key=True, serialize=False)),
                ('severity', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('assigned_to', models.CharField(max_length=100)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('reported_by', models.CharField(max_length=100)),
                ('reported_at', models.DateTimeField()),
                ('assigned_at', models.DateTimeField()),
                ('priority', models.CharField(max_length=20)),
                ('due_date', models.DateField()),
                ('resolved_by', models.CharField(max_length=100)),
                ('resolution', models.TextField()),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_analysis.log')),
            ],
        ),
    ]
