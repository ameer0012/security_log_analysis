# Create your models here.
from django.db import models


class LogEvent(models.Model):
    timestamp = models.DateTimeField(),
    level = models.CharField(max_length=50),
    user_id = models.IntegerField(null=True),
    user_name = models.CharField(max_length=100, null=True),
    user_email = models.EmailField(null=True),
    tags = models.TextField(null=True),
    source = models.CharField(max_length=100),
    objects = models.Manager(),
    message = models.TextField()

    def __str__(self):
        return f"LogEvent: {self.timestamp} - {self.level}"


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=100)
    message = models.TextField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=200)
    log_type = models.CharField(max_length=50)
    log_category = models.CharField(max_length=50)
    user_id = models.IntegerField()
    request_path = models.CharField(max_length=200)
    response_status = models.IntegerField()

class Incident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    severity = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20)
    assigned_to = models.CharField(max_length=100)
    resolved_at = models.DateTimeField(null=True, blank=True)
    reported_by = models.CharField(max_length=100)
    reported_at = models.DateTimeField()
    assigned_at = models.DateTimeField()
    priority = models.CharField(max_length=20)
    due_date = models.DateField()
    resolved_by = models.CharField(max_length=100)
    resolution = models.TextField()

class ThreatIntelligence(models.Model):
    threat_id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)
    description = models.TextField()
    last_updated = models.DateTimeField()
    confidence_level = models.CharField(max_length=20)
    indicator = models.CharField(max_length=100)
    confidence = models.CharField(max_length=20)
    source_url = models.URLField()
    additional_info = models.TextField()

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    reviewed_by = models.CharField(max_length=100)
    reviewed_at = models.DateTimeField()
    attachment = models.FileField(upload_to='attachments/')

    def __str__(self):
        return self.title
