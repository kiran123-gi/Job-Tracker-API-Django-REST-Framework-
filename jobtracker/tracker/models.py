from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),
    ]

    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    applied_date = models.DateField()
    interview_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    applied_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.company_name
