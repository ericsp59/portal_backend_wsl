from django.db import models
from tabnanny import verbose
# Create your models here.


class PortalJobsLog(models.Model):
    job_dt = models.DateTimeField(auto_now=True)
    job_template_name = models.CharField(max_length=200, verbose_name="Шаблон")
    job_template_keys = models.CharField(max_length=200, verbose_name="Учетные данные")

    def __str__(self):
        return self.job_template_name

    class Meta:
        verbose_name = "лог"  
        verbose_name_plural = "логи" 
