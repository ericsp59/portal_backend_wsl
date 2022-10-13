from rest_framework.response import Response
from portal_logs.models import PortalJobsLog
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from django.forms import model_to_dict

from .models import PortalJobsLog
from .serializers import PortalLogsSerializer
# Create your views here.


class PortalLogsApiView(APIView):
    def get(self, request):
        log_list = PortalJobsLog.objects.all().values()
        print(log_list)
        return Response({'logs': list(log_list)})

    def post(self, request):
        post_new = PortalJobsLog.objects.create(
            job_template_name = request.data['job_template_name'],
            job_template_keys = request.data['job_template_keys']
        )
        return Response({'post': model_to_dict(post_new)})


# class PortalLogsApiView(generics.ListAPIView):
#     queryset = PortalJobsLog.objects.all()
#     serializer_class = PortalLogsSerializer
