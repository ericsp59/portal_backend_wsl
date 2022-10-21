import subprocess
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import PortalFrontSettings, PortalGlpiSettings, PortalSemaphoreSettings
from rest_framework.renderers import JSONRenderer
from .dbconnection import getDevicesFromDb, getNetDeviceInfoById, getPhoneInfoById, getComputerInfoById, get_ip_addresses
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import NoteSerializer, GlpiSettingsSerializer
from .models import Note


# Create your views here.

class PortalGetDeviceIpByIdFromDbApiView(APIView):
    def get(self, request):
        id = str(request.headers['ID'])
        type = str(request.headers['Type'])
        return Response({"get": "ok", "data": get_ip_addresses(type, id)}) 

class PortalGetComputerInfoByIdFromDbApiView(APIView):
    def get(self, request):
        id = str(request.headers['ID'])
        return Response({"get": "ok", "data": getComputerInfoById(id)})  

class PortalGetPhoneInfoByIdFromDbApiView(APIView):
    def get(self, request):
        id = str(request.headers['ID'])
        return Response({"get": "ok", "data": getPhoneInfoById(id)})    

class PortalGetNetDevInfoByIdFromCbApiView(APIView):
    def get(self, request):
        id = str(request.headers['ID'])
        return Response({"get": "ok", "data": getNetDeviceInfoById(id)})    


class PortalGetDevicesFromDbApiView(APIView):

    def get(self, request):
        type = str(request.headers['Type'])
        return Response({"get": "ok", "data": getDevicesFromDb(type)})


def upload_func(name,file):
    with open(name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

class PortalGlpiApiView(APIView):
    parser_classes = [JSONParser]
    def get(self, request):
        # glpi_settings = PortalGlpiSettings.objects.all()
        glpi_settings = PortalGlpiSettings.objects.get(glpi_srv_name="glpi")
        # print(type(glpi_settings))
        # serializer = GlpiSettingsSerializer(glpi_settings, many=True)
        # print(serializer)
        # print(serializer.data)
        return Response({"get": "ok", "data": {
            "glpi_api_url":glpi_settings.glpi_api_url,
            "glpi_user_token":glpi_settings.glpi_user_token,
            "glpi_app_token":glpi_settings.glpi_app_token
        }})

class PortalSemaphoreApiView(APIView):
    parser_classes = [JSONParser]
    def get(self, request):
        semaphore_settings = PortalSemaphoreSettings.objects.get(semaphore_srv_name="semaphore")
        return Response({"get": "ok", "data": {
            "semaphore_api_url":semaphore_settings.semaphore_api_url,
            "semaphore_user_login":semaphore_settings.semaphore_user_login,
            "semaphore_user_password":semaphore_settings.semaphore_user_password,
            "semaphore_user_token":semaphore_settings.semaphore_user_token
        }})




class PortalFrontApiView(APIView):
    
    parser_classes = [FileUploadParser]
    def post(self, request):
        
        settings = PortalFrontSettings.objects.get(semaphore_srv_name="semaphore")
        name = request.data['file'].name

        file = request.FILES.get('file')
        upload_func(name, file)

        # #### localhost
        # upload_func(f'/{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir}/playbooks/{name}', file)

        # command = subprocess.run(["ssh", f'{settings.semaphore_srv_user}@localhost', f"cd /{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir} && git add * && git commit -am '123' && git push"])
        # ####

        command = subprocess.run([f'scp', f'{name}', f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}:/{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir}/playbooks'])

        command = subprocess.run(["ssh", f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}', f"cd /{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir} && git add * && git commit -am '123' && git push"])

        ####
        # D:/DISTR/utils/pscp/pscp.exe

        ## WIN
        ##command = subprocess.run([f'{settings.copy_files_program}','-pw', 'root', name, f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}:/{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir}/playbooks'], shell=True)

        ##command = subprocess.run(["ssh",f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}',f'-i {settings.semaphore_srv_priv_key_file}', "bash syncgit.sh"], shell=True)
        print("The exit code was: %d" % command.returncode)
        return Response({'post': 'ok', 'name': name})
     

    @api_view(['GET'])
    def getRoutes(request):
        routes = [
            '/api/token',
            '/api/token/refresh',
        ]
        return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    # notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
