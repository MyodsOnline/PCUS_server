from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import PCUS, OBJ
from .serializers import OBJModelSerializer, PCUSModelSerializer


class OBJModelViewSet(ModelViewSet):
    queryset = OBJ.objects.all()
    serializer_class = OBJModelSerializer


class PCUSModelViewSet(ModelViewSet):
    queryset = PCUS.objects.all()
    serializer_class = PCUSModelSerializer


def get_test_data(request):
    obj_test_data = OBJ.objects.all().order_by('title')
    pcus_test_data = PCUS.objects.all().order_by('title')
    context = {
        'obj_test_data': obj_test_data,
        'pcus_test_data': pcus_test_data,
    }
    return render(request, 'base.html', context)
