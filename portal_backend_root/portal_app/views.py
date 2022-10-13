from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@permission_classes([IsAuthenticated])
def portal_app(request):
    return render(request, './portal/index.html')
