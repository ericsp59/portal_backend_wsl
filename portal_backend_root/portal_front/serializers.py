from rest_framework import serializers 


from portal_front.models import Note, PortalGlpiSettings

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class GlpiSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalGlpiSettings
        fields = '__all__'       


