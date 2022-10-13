from portal_logs.models import PortalJobsLog
from rest_framework import serializers
from .models import PortalJobsLog


class PortalLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalJobsLog
        fields = ('job_dt', 'job_template_name', 'job_template_keys')
