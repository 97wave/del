from rest_framework.viewsets import ModelViewSet
from .models import Measurement, Project
from .serializers import MeasurementModelSerializer, ProjectModelSerializer



class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения.""" 
    queryset = Measurement.objects.all()
    serializer_class = MeasurementModelSerializer

