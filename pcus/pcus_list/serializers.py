from rest_framework.serializers import HyperlinkedModelSerializer
from .models import PCUS, OBJ


class OBJModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OBJ
        fields = '__all__'


class PCUSModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PCUS
        fields = '__all__'
