from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class ModelInfo(models.Model):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    use_cases = models.TextField()
    practices = models.TextField()
    data_info = models.TextField(blank=True, null=True)
    concerning_practices = models.TextField(blank=True, null=True)
    concerning_practices_urls = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], blank=True, null=True)

    def __str__(self):
        return self.name
    def colored_severity(self):
        if self.severity == 'low':
            color = 'green'
        elif self.severity == 'medium':
            color = 'orange'
        elif self.severity == 'high':
            color = 'red'
        else:
            color = 'black'  # Default color if severity is not set

        severity_display = self.severity.capitalize() if self.severity else 'Unknown'
        return format_html('<span style="color: {};">{}</span>', color, severity_display)
    
    colored_severity.short_description = 'Severity'  # Display name in admin
    def formatted_concerning_practices_urls(self):
        # Check if concerning_practices_urls is not None and has content
        if self.concerning_practices_urls:
            urls = self.concerning_practices_urls.split(',')
            links = ''.join([f'<a href="{url.strip()}" target="_blank">{url.strip()}</a><br>' for url in urls if url.strip()])
            return format_html(links)
        return format_html('<span>No URLs provided</span>')  # Fallback if there are no URLs

    
    formatted_concerning_practices_urls.short_description = 'Concerning Practices Links'

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelInfo, on_delete=models.CASCADE)
    preference = models.TextField()